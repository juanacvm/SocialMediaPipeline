# Pandas - Proyecto ETL en JSON Placeholder

Proyecto pipeline ETL que consume datos de la API JSONPlaceholder y que, mediante un proceso de transformación gracias a pandas, se carga a SQL haciendo uso de la librería SQLAlchemy.

## 📋 Descripción

El presente proyecto cumple con el procedimiento de:
Extraer los datos de la API Json Placeholder
Transformar los datos mediante pandas
Cargar los datos empleando SQLAlchemy

- Usuarios (Users)
- Tareas (Todos)
- Publicaciones (Posts)
- Comentarios (Comments)
- Álbumes (Albums)
- Fotos (Photos)


## 🏗️ Estructura

```
src/
├── config.py       # Carga las variables de entorno
├── database.py     # Establece la conexión SQL
├── models.py       # Genera los modelos ORM
├── etl_logic.py    # Extracción y transformación de datos
└── main.py         # Pipeline principal de ejecución del proyecto
```

## 🛠️ Requisitos

- Python 3.8+
- SQL Server + ODBC Driver 17

## 📦 Instalación

1. Modifica `.env.example` a `.env` y completa las credenciales:
```env
DB_DRIVER=Tu_sql_driver, puede ser: ODBC Driver 17 for SQL Server
DB_SERVER=tu_servidor
DB_NAME=base_datos_destino
DB_USER=usuario
DB_PASSWORD=contraseña
```

2. Instala dependencias:
```bash
pip install -r requirements.txt
```

## 🚀 Uso

```bash
python src/main.py
```

Crea/recrea las tablas y carga datos desde JSONPlaceholder.

## 📊 Tablas

| Tabla | Descripción |
|-------|-------------|
| Users | Usuarios registrados |
| Todos | Tareas registradas por el usuario, ya sea completada o no |
| Posts | Publicaciones registradas por los usuarios |
| Comments | Comentarios de cada post |
| Albums | Álbumes de fotos levantadas por los usuarios|
| Photos | Fotos con enlace URLs hacia ellas |

## ⚠️ Importante

- Las tablas se recrean cada ejecución
- Requiere conexión a internet para conectarse y extraer datos de JSONPlaceholder
