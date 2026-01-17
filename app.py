from fastapi import FastAPI
# Aquí conectamos con la nueva estructura de carpetas
from api.routers.tareas import router as tareas_router

app = FastAPI(title="Mi App de FastAPI")

# Esto es lo que hace que aparezcan en /docs
app.include_router(tareas_router)

@app.get("/")
def read_root():
    return {"message": "Hola Vicente, el servidor está corriendo"}