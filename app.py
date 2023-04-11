from fastapi import FastAPI, Request
from conect_mysql import obtener_conexion
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
# Create model for post
class Formulario(BaseModel):
    aspiracion: str
    cargo_asp: str
    actividad_mil: str
    tipo_doc: str
    num_doc: str
    fecha_exp: str
    ciudad_exp: str
    nombres: str
    apellidos: str
    genero: str
    fecha_nacimiento: str
    estudios: str
    oficio: str
    tip_poblacion: str
    num_celular: str
    correo:str
    pais:str
    departamento: str
    municipio: str
    dir_recidencia: str
    localidad: str


@app.post("/formulario")
async def post_formulario(formulario: Formulario):
    return formulario

    