from logging import basicConfig
from database import Pelicula, User
from pydantic import BaseModel

class Peliculas(BaseModel):
    nombre: str
    genero: str
    año: str

class Users(BaseModel):
    userName: str
    email: str
    password: str

class Peliculas2(BaseModel):
    userMovie: str
    nombre: str
    genero: str
    actor: str


class Peliculas2Id(Peliculas2):
    id: int






class PeliculasId(Peliculas):
    id: int


class UsersId(Users):
    id: int


class BorrarPeliculas(Peliculas):
    id: int

