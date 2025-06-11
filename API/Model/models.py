# API/Models/models.py
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from API.Persistence.database import Base

# Tabela de associacao entre tarefas e usuarios
tarefa_usuario = Table(
    'tarefa_usuario',
    Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id')),
    Column('tarefa_id', Integer, ForeignKey('tarefas.id'))
)

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)

    tarefas = relationship("Tarefa", secondary=tarefa_usuario, back_populates="usuarios")


class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    status = Column(String, default="pendente")

    usuarios = relationship("Usuario", secondary=tarefa_usuario, back_populates="tarefas")

