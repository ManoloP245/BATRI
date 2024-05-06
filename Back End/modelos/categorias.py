from sqlalchemy import Column, Integer, String
from conexiondb.database import Base

class Categorias(Base):
    __tablename__ = 'categorias'
    id_categoria = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    descripcion = Column(String(500))
    estado = Column(Integer)

    def __init__(self, nombre=None, descripcion=None,estado=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

