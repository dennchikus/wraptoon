from sqlalchemy import select

from src.models.details import DetailsORM
from src.repositories.base import BaseRepository
from src.schemas.details import Details

class DetailsRepository(BaseRepository):
    model = DetailsORM
    schema = Details

    async def get_filtered_by_name(self, name_detail: str | None):
        query = select(self.model)
        if name_detail is not None:
            query = query.filter(
                self.model.name_detail.ilike(f"%{name_detail}%")
            )
        result = await self.session.execute(query)
        return [self.schema.model_validate(model, from_attributes=True) for model in result.scalars().all()]


