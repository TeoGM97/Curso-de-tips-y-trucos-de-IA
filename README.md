# API con FastAPI

Este proyecto es una API desarrollada con FastAPI.

## Requisitos

- Python 3.8 o superior
- uv (gestor de paquetes y entornos virtuales)

## Instalación

1. Clona este repositorio:

```bash
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
```

2. Crea un entorno virtual e instala las dependencias con uv:

```bash
uv venv
uv pip install -r requirements.txt
```

## Ejecución

Para ejecutar la API en modo desarrollo:

```bash
python run.py
```

O directamente con uvicorn:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`.

## Documentación

La documentación automática estará disponible en:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc` 