from sqlalchemy import select, insert

from src.models.services_details import ServicesDetailsORM
from src.models.details import DetailsORM
from src.models.services import ServicesORM
from src.repositories.base import BaseRepository
from src.schemas.services_details import ServiceDetail, ReadableServiceDetails

class ServicesDetailsRepository(BaseRepository):
    model = ServicesDetailsORM
    schema = ServiceDetail


    async def add_by_names(
            self,
            name_detail: str,
            name_service: str,
            price: int
    ):
        detail_id = (
            select(DetailsORM.id)
            .select_from(DetailsORM)
            .filter(DetailsORM.name_detail == name_detail)
            .scalar_subquery()
        )

        service_id = (
            select(ServicesORM.id)
            .select_from(ServicesORM)
            .filter(ServicesORM.name_service == name_service)
            .scalar_subquery()
        )

        result = (
            insert(ServicesDetailsORM)
            .values(service_id=service_id, detail_id=detail_id, price=price)
        )

        await self.session.execute(result)

    async def get_readable_all_relationships(self, ids: list[int] | None = None):

        names_details_and_services = (
            select(
                self.model.id,
                DetailsORM.name_detail.label("name_detail"),
                ServicesORM.name_service.label("name_service"),
                self.model.price
            )
            .select_from(self.model)
            .join(DetailsORM, DetailsORM.id == self.model.detail_id)
            .join(ServicesORM, ServicesORM.id == self.model.service_id)
        )

        if ids is not None:
            names_details_and_services = names_details_and_services.filter(self.model.id.in_(ids))

        result = await self.session.execute(names_details_and_services)
        return [ReadableServiceDetails.model_validate(model) for model in result.mappings().all()]
