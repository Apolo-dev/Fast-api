from fastapi import FastAPI,HTTPException
from typing import Optional
from peewee import *

from pydantic.errors import PathNotExistsError
from database import database as connection
from database import Pelicula, User, Pelicula2
from schemas import Peliculas, Users, Peliculas2, PeliculasId, UsersId, Peliculas2Id


app = FastAPI()

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    
    connection.create_tables([Pelicula])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

#metodos post

@app.post('/peliculas')
async def guardarPelicula(peliculas:Peliculas):
    peliculitas = Pelicula.create(
        nombre=peliculas.nombre,
        genero=peliculas.genero,
        año=peliculas.año
    )
    return peliculitas

@app.post('/usuarios')
async def guardarUsuario(usuarios:Users):
    usuarios = User.create(
        userName=usuarios.userName,
        email=usuarios.email,
        password=usuarios.password
    )
    return usuarios

@app.post('/peliculas2')
async def guardarPeliculas2(peliculas2:Peliculas2):
    peliculas2 = Pelicula2.create(
        userMovie=peliculas2.userMovie,
        nombre=peliculas2.nombre,
        genero=peliculas2.genero,
        actor=peliculas2.actor
    )
    return peliculas2


# metdos get

@app.get('/peliculas')
async def verPeliculas():
    for pelis in Pelicula.select():
            print ([pelis])
            return pelis


@app.get('/peliculas/{item_id}')
async def traerpeliculas(item_id: str):
    pelis = Pelicula.select().where(Pelicula.id == item_id).first()
    if pelis:
        return PeliculasId(
            id = pelis.id,
            nombre = pelis.nombre,
            genero = pelis.genero,
            año = pelis.año

        )
    else:
        return HTTPException(404, 'user not found')


@app.get('/usuarios/{item_id}')
async def traerUsuario(item_id: str):
    usuario = User.select().where(User.id == item_id).first()
    if usuario:
        return UsersId(
            id = usuario.id,
            userName = usuario.userName,
            email= usuario.email,
            password = usuario.password
        )
    else:
        return HTTPException(404, 'user not found')




        


