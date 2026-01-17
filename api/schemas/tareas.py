from pydantic import BaseModel

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: str
    fecha_creacion: str
    fecha_vencimiento: str
    estado: str
    prioridad: str

class TareaResumida (BaseModel):
    nombre: str
    apellido: str