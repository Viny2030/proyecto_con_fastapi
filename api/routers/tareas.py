from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.data.base_de_datos import tabla_tareas
from api.schemas.tareas import TareaResumida, Tarea

router = APIRouter(
    prefix="/tareas",
    tags=['Tareas']
)

# 1. Endpoint: Listar todas (Sin Pydantic)
@router.get("/")
def get_tareas_sin_pydantic() -> list[dict]:
    return tabla_tareas

# 2. Endpoint: Listar todas (Con Pydantic)
# CORRECCIÓN: Se usa list[Tarea], no list(Tarea)
@router.get("/pydantic", response_model=list[Tarea])
def get_tareas_con_pydantic():
    return tabla_tareas

# 3. Endpoint: Obtener una tarea por ID
@router.get("/{tarea_id}")
def get_tarea(tarea_id: int):
    for tarea in tabla_tareas:
        if tarea["id"] == tarea_id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# 4. Endpoint: Resumen manual
@router.get("/resumen/{tarea_id}")
def get_tarea_resumida_sin_pydantic(tarea_id: int) -> dict:
    for tarea in tabla_tareas:
        if tarea["id"] == tarea_id:
            return {"id": tarea['id'], "titulo": tarea["titulo"]}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# 5. Endpoint: Resumen con Pydantic
# CORRECCIÓN: Se usa TareaResumida (que es la que importaste arriba)
@router.get("/pydantic/resumen/{tarea_id}", response_model=TareaResumida)
def get_tarea_resumida_con_pydantic(tarea_id: int):
    for tarea in tabla_tareas:
        if tarea["id"] == tarea_id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@router.get("/pydantic/busqueda", response_model=list[Tarea])
def get_tareas_con_pydantic_y_filtro(
        estado: str
):
    return [tarea for tarea in tabla_tareas if tarea["estado"] == estado]