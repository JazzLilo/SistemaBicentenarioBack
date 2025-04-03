from fastapi import Depends
from src.infrastrucutre.conecction import PrismaSingleton

async def get_conecction():
    client = PrismaSingleton.get_db()
    yield client
        