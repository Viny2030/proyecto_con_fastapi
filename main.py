from fastapi import FastAPI
# Importamos usando la nueva ruta de la carpeta
from api.routers.tareas import router as tareas_router

app = FastAPI(title="Mi App de FastAPI")
app.include_router(tareas_router)

app = FastAPI(
    title="Mi App de FastAPI",
    description="Esta es una descripción general de mi API para el examen de Humai"
)

# ESTA ES LA LÍNEA QUE FALTA PARA QUE APAREZCAN LOS ENDPOINTS
app.include_router(tareas_router)

@app.get("/")
def read_root():
    return {"message": "Mi primera app con FastAPI, soy vicente"}