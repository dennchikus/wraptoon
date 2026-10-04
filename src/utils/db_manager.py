from src.repositories.details import DetailsRepository
from src.repositories.services import ServiceRepository
from src.repositories.services_details import ServicesDetailsRepository

class DBManager():
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.services = ServiceRepository(self.session)
        self.details = DetailsRepository(self.session)
        self.services_details = ServicesDetailsRepository(self.session)

        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()