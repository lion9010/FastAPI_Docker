# 🚀 API FastAPI con Docker

Este proyecto es un ejemplo sencillo de una API creada con **FastAPI** y ejecutada dentro de un contenedor **Docker**.  
Utiliza un diccionario como base de datos simulada y expone un CRUD básico de productos.

---

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- **Git**
- **Docker** (Docker Desktop o Docker Engine)

🖐 Si vas a ejecutar el proyecto desde un entorno de desarrollo en la nube (por ejemplo, GitHub Codespaces), no necesitas instalar nada de lo anterior.

## 1. Clonar el repositorio

```bash
git clone https://github.com/reinaldodu/FastAPI_Docker.git
```
Ingresar al directorio del proyecto:
```bash
cd FastAPI_Docker
```

## 2. Construir la imagen Docker
Desde la raíz del proyecto ejectuar el comando:
```bash
docker build -t fastapi .
```

## 3. Ejecutar el contenedor
```bash
docker run --name fastapi -p 8000:8000 fastapi
```

La API quedará disponible en:

👉 http://localhost:8000

🖐 En entornos en la nube (como GitHub Codespaces), la plataforma genera automáticamente la URL pública para acceder a la API.

## 4. Pruebas y documentación interactiva (Swagger UI)
FastAPI incluye **Swagger**, que es un conjunto de herramientas que sirve para documentar y probar APIs de manera interactiva.

Accede desde tu navegador para ver la documentación y hacer pruebas a la API:

👉http://localhost:8000/docs

🖐 En entornos en la nube, usa la URL pública asignada seguida de /docs.
