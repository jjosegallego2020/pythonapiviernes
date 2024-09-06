from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship 
from sqlalchemy.ext.declarative import declarative_base

#Crear una variable de la base para crear tables

Base=declarative_base() 

# listado de modelos de la aplicación

# USUARIO
class Usuario(Base):
    __tablename__='usuarios'
    id=Column (Integer,primary_key=True, autoincrement=True)
    name=Column(String(50))
    age=Column(Integer())
    phone=Column(String(12))
    email=Column(String(20))
    password=Column(String(10))
    signUpDate=Column(Date)
    ciudad =Column(String(50))

# GASTO
    class Gasto(Base):
     __tablename__='Gastos'
     id=Column(Integer,primary_key=True, autoincrement=True)
     monto=Column(Integer)
     fecha=Column(Date)
     descripcion=Column(String)
     nombre=Column(String)
     


# CATEGORIA
    class Categoria(Base):
        __tablename__='categoria'
        id=Column(Integer,primary_key=True, autoincrement=True)
        nombrecategoria=Column(String())
        descripcion=Column(String())
        fotoicono=Column(String())

# METODO DE PAGO
    class MetodoPago(Base):
       __tablename__='metodo_pago'
       id=Column(Integer)
       nombremetodo=Column()
       descripcion=Column()

# FACTURA
    class Factura(Base):
       __tablename__='factura'
      
       #id
       #
       #


