from src.models.services_details import ServicesDetailsORM
from src.repositories.base import BaseRepository
from src.schemas.services_details import ServiceDetail

class ServicesDetailsRepository(BaseRepository):
    model = ServicesDetailsORM
    schema = ServiceDetail