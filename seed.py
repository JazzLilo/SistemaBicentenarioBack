import asyncio
from prisma import Prisma

async def seed_roles():
    prisma = Prisma()
    await prisma.connect()

    roles = [
        {"nombre_rol": "usuario", "descripcion": "usuario", "id": 1},
        {"nombre_rol": "administrador", "descripcion": "admin", "id": 2},
        {"nombre_rol": "cultural", "descripcion": "cultural", "id": 3},
        {"nombre_rol": "academico", "descripcion": "academico", "id": 4},
        {"nombre_rol": "organizador", "descripcion": "organizador", "id": 5},
        {"nombre_rol": "controlador", "descripcion": "controlador", "id": 6},
    ]

    for role in roles:
        # Usamos upsert para crear o actualizar si ya existe
        await prisma.rol.upsert(
            where={"id": role["id"]},
            data={
                "create": role,
                "update": role
            }
        )

    print("Roles seeded successfully!")
    await prisma.disconnect()

if __name__ == "__main__":
    asyncio.run(seed_roles())