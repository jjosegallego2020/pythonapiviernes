from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#crear una instancia de la base para crear tablas
Base = declarative_base()

#listado de modelos de la aplicacion
#usuario
class Usuario(Base):
    __tablename__="usuarios"
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(50))
    age=Column(Integer)
    phone=Column(String (12))
    email=Column(String(20))
    password=Column(String(10))
    registrationDate=Column(Date)
    city=Column(String(50))

#gasto
class Gasto(Base):
    __tablename__="gastos"
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Float)
    fecha=Column(Date)
    descripcion=Column(String(100))
    nombre=Column(String(50))

#categoria
class Categoria(Base):
    __tablename__="categoria"
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(50))
    descripcion=Column(String(100))
    fotoIcono=Column(String(100))



#metodos de pago
class MetodoPago(Base):
    __tablename__="metodo_pago"
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(50))
    descripcion=Column(String(100))

#factura
class Factura(Base):
    pass
