from prisma import Prisma
import asyncio

class PrismaSingleton:
    _instance = None
    _lock = asyncio.Lock()

    def __init__(self):
        self.db = Prisma()

    @classmethod
    async def get_db(cls):
        if cls._instance is None:
            async with cls._lock:
                if cls._instance is None:
                    cls._instance = PrismaSingleton()
                    await cls._instance.db.connect()
        return cls._instance.db

async def get_connection():
    db = await PrismaSingleton.get_db()
    try:
        yield db
    finally:
        # Don't disconnect here to maintain connection pool
        pass