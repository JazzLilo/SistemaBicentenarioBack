from prisma import Prisma

class PrismaSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PrismaSingleton, cls).__new__(cls)
            cls._instance.db = Prisma()
        return cls._instance

    @staticmethod
    async def get_db():
        instance = PrismaSingleton()
        if not instance._instance.db.is_connected():
            await instance._instance.db.connect()
        return instance._instance.db
