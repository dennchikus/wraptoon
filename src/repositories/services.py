from src.models.services import ServicesORM
from src.repositories.base import BaseRepository
from src.schemas.services import Service

class ServiceRepository(BaseRepository):
    model = ServicesORM
    schema = Service

