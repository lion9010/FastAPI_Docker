from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="API de Productos",
    description="Documentación de la API para la gestión de productos.",
    version="1.0.0"
)

# Modelo Pydantic
class Producto(BaseModel):
    id: int
    nombre: str
    precio: float

# "Base de datos" simulada
productos = {
    1: {"id": 1, "nombre": "Laptop", "precio": 3500.0},
    2: {"id": 2, "nombre": "Teclado", "precio": 120.0},
    3: {"id": 3, "nombre": "Mouse", "precio": 45.5},
    4: {"id": 4, "nombre": "Monitor", "precio": 900.0},
    5: {"id": 5, "nombre": "Audífonos", "precio": 150.0},
    6: {"id": 6, "nombre": "Webcam", "precio": 200.0},
}

# Ruta raíz
@app.get("/")
def root():
    return {"message": "API FastAPI en Docker funcionando"}

# Listar los productos
@app.get("/productos")
def get_productos():
    return list(productos.values())

# Listar un producto
@app.get("/productos/{producto_id}")
def get_producto(producto_id: int):
    if producto_id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return productos[producto_id]

# Crear un producto
@app.post("/productos")
def create_producto(producto: Producto):
    if producto.id in productos:
        raise HTTPException(status_code=400, detail="El ID ya existe")
    productos[producto.id] = producto.dict()
    return {"message": "Producto creado", "item": producto}

# Actualizar un producto
@app.put("/productos/{producto_id}")
def update_producto(producto_id: int, producto: Producto):
    if producto_id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if producto_id != producto.id:
        raise HTTPException(status_code=400, detail="El ID del producto no coincide con la URL")

    productos[producto_id] = producto.dict()
    return {"message": "Producto actualizado", "item": producto}

# Eliminar un producto
@app.delete("/productos/{producto_id}")
def delete_producto(producto_id: int):
    if producto_id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    eliminado = productos.pop(producto_id)
    return {"message": "Producto eliminado", "item": eliminado}
