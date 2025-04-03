from prisma import Prisma
from typing import List, Optional
from prisma.models import UserTest

async def get_users(db: Prisma) -> List[UserTest]:
    """Obtiene todos los usuarios de la base de datos"""
    try:
        return await db.usertest.find_many()
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
        return []