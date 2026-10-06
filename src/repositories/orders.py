from src.models.orders import OrdersORM
from src.repositories.base import BaseRepository
from src.schemas.orders import Orders

class OrdersRepository(BaseRepository):
    model = OrdersORM
    schema = Orders