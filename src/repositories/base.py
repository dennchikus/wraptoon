from pydantic import BaseModel
from sqlalchemy import select, insert, update, delete


class BaseRepository():
    model = None
    schema: BaseModel = None

    def __init__(self, session):
        self.session = session


    # GET by name

    async def get_filtered(self, *filter, **filter_by):
        query = (
            select(self.model)
            .filter(*filter)
            .filter_by(**filter_by)
        )
        result = await self.session.execute(query)
        return [self.schema.model_validate(model, from_attributes=True) for model in result.scalars().all()]

    async def get_all(self):
        return await self.get_filtered()

    async def get_one_or_none(self, **filter_by):
        query = (
            select(self.model)
            .filter_by(**filter_by)
        )
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()
        if model is not None:
            return self.schema.model_validate(model, from_attributes=True)
        return None

    async def add(self, data: BaseModel):
        query = (
            insert(self.model)
            .values(**data.model_dump())
            .returning(self.model)
        )
        result = await self.session.execute(query)
        model = result.scalars().one()
        return self.schema.model_validate(model, from_attributes=True)

    async def edit(self, data: dict):
        values = dict(data)
        item_id = values.pop("id", None)
        query = (
            update(self.model)
            .values(**values)
            .filter_by(id=item_id)
            .returning(self.model)
        )
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()
        if model is not None:
            return self.schema.model_validate(model, from_attributes=True)
        return None

    async def delete(self, **filter_by):
        query = (
            delete(self.model)
            .filter_by(**filter_by)
        )
        await self.session.execute(query)