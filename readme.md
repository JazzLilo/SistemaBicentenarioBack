# Configuración del Entorno y Ejecución del Proyecto

## 1. Crear y Activar el Entorno Virtual

Primero, crea un entorno virtual de Python para aislar las dependencias del proyecto:

```sh
python -m venv venv
```

Luego, activa el entorno:

- En Windows:
  ```sh
  venv\Scripts\activate
  ```
- En macOS/Linux:
  ```sh
  source venv/bin/activate
  ```

## 2. Instalar Dependencias

Con el entorno activado, instala las dependencias necesarias:

```sh
pip install -r requirements.txt
```

## 3. Configurar la Base de Datos

Ejecuta el siguiente comando para aplicar las migraciones con Prisma:

```sh
python -m prisma db push
```

## 4. Cargar Roles en la Base de Datos

Para insertar los roles en la base de datos, ejecuta:

```sh
python seed.py
```

## 5. Ejecutar el Proyecto

Finalmente, presiona **F5** en tu editor de código (por ejemplo, VS Code) para iniciar la ejecución del proyecto.