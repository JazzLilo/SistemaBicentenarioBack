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


async def seed_categorias():
    categorias_base = [
        {"nombre_categoria": "Bélico", "descripcion": "Batallas, guerras y conflictos armados"},
        {"nombre_categoria": "Tratados", "descripcion": "Acuerdos diplomáticos y pactos"},
        {"nombre_categoria": "Científico", "descripcion": "Descubrimientos e innovaciones"},
        {"nombre_categoria": "Revoluciones", "descripcion": "Movimientos sociales y políticos"},
        {"nombre_categoria": "Independencia", "descripcion": "Procesos de liberación nacional"}
    ]
    
    prisma = Prisma()
    await prisma.connect()
    
    for categoria in categorias_base:
        # First try to find if the category exists
        existing = await prisma.categoria.find_unique(
            where={"nombre_categoria": categoria["nombre_categoria"]}
        )
        
        if existing:
            # Update if exists
            await prisma.categoria.update(
                where={"nombre_categoria": categoria["nombre_categoria"]},
                data=categoria
            )
        else:
            # Create if doesn't exist
            await prisma.categoria.create(data=categoria)
    
    print("Categorías sembradas exitosamente!")
    await prisma.disconnect()    

if __name__ == "__main__":
    asyncio.run(seed_categorias())