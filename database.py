from peewee import *

database = MySQLDatabase(
    'peliculas',
    user='root',
    password = 'Chileylau020',
    host = 'localhost',
    port = 3306
)

class Pelicula(Model):
    nombre = CharField(max_length=50)
    genero = CharField(max_length=20)
    año = CharField(max_length=20)

    def __str__(self):
        return self.nombre

    class Meta:
        database = database
        table_name = 'peliculas'


# base de datos del usuario

class User(Model):
    userName = CharField(max_length=45)
    email = CharField(max_length=45)
    password = CharField(max_length=45)

    def __str__(self):
        return self.email

    class Meta:
        database = database
        table_name = 'usuarios'


# base de datos peliculas 2

class Pelicula2(Model):
    userMovie = ForeignKeyField(User, backref='peliculas2')
    nombre = CharField(max_length=45)
    genero = CharField(max_length=45)
    actor = CharField(max_length=45)

    def __str__(self):
        return self.genero

    class Meta:
        database = database
        table_name = 'peliculas2'







