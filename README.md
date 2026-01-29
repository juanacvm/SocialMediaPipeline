# Pipeline ETL para la carga de JSONPlaceholder con Pandas y SQLAlchemy

## Descripción

Proyecto que implementa un pipeline que cumple con los estándares ETL utilizando Python. Consume datos de una API, transforma y normaliza los datos mediante pandas y los guarda en SQL mediante SQLAlchemy.

## Características

- **Separación de responsabilidades:** Asignación de métodos a distintos archivos para separar la lógica del proceso ETL y tener un mejor mantenimiento del código.

- **Extracción eficiente:** Consumo de API mediante requests y manejo de `.env` para controlar errores ante caídas de red.

- **Seguridad:** Gestión de credenciales mediante variables de entorno `.env` para evitar el hardcodeo de información sensible en el código fuente.

- **Integración robusta a SQL:** Manejo de SQLAlchemy ORM para la creación y gestión de tablas SQL.

## Arquitectura del Pipeline

El pipeline sigue el procedimiento ETL estándar:

```
Conexión con API JSONPlaceholder → Extracción → Transformación → Carga (SQL Server)
```

## Tecnologías Utilizadas

- **Python 3.8+**
- **Pandas**: Para carga, limpieza y transformación de datos
- **SQLAlchemy**: Para la gestión de base de datos (ORM)
- **Requests**: Para consumir APIs.
- **Python-dotenv**: Para la configuración de entorno
- **SQL Server**: Para la gestión de base de datos relacionales

## Estructura del Proyecto

```
PandasPracticeRequests/
├── src/
│   ├── main.py                         # Script que ejecuta pipeline
│   ├── config.py                       # Configuración de variables de entorno
│   ├── database.py                     # Conexión a la BD
│   ├── models.py                       # Modelos ORM de tablas
│   └── etl_logic.py                    # Lógica ETL (Carga de API y transformación)
├── requirements.txt                    # Archivo para instalar librerías Python
└── README.md                           # Este archivo
```

## Tablas implementadas

| Tabla | Descripción |
|-------|-------------|
| Users | Usuarios registrados |
| Todos | Tareas registradas por el usuario, ya sea completada o no |
| Posts | Publicaciones registradas por los usuarios |
| Comments | Comentarios de cada post |
| Albums | Álbumes de fotos levantadas por los usuarios |
| Photos | Fotos con enlace URLs hacia ellas |

## Prerequisitos

- Python 3.11 o superior
- SQL Server 2019 o superior instalado
- Git para clonar el repositorio
- Pip (Gestor de paquetes de Python)
- Conexión a internet para acceder a JSONPlaceholder API

## Configuración e Instalación

### Instalación:

1. **Clona el repositorio**
```bash
git clone https://github.com/juanacvm/socialmedia-pipeline.git
cd socialmedia-pipeline-main
```


2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Configurar variables de entorno (reemplazar `.env.example` por `.env`):**
```env
DB_DRIVER=ODBC Driver 17 for SQL Server
DB_SERVER=tu_servidor
DB_NAME=nombre_base_datos
DB_USER=usuario
DB_PASSWORD=contraseña
```

4. **Ejecutar el pipeline:**
```bash
python src/main.py
```