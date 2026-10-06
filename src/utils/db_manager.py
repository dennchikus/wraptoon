from src.repositories.details import DetailsRepository
from src.repositories.services import ServicesRepository
from src.repositories.services_details import ServicesDetailsRepository
from src.repositories.orders import OrdersRepository

class DBManager():
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.services = ServicesRepository(self.session)
        self.details = DetailsRepository(self.session)
        self.services_details = ServicesDetailsRepository(self.session)
        self.orders = OrdersRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()