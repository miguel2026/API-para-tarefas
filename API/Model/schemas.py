# API/Models/schemas.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date

# ---------- Tarefa ----------
class TarefaBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    status: Optional[str] = "pendente"


class TarefaCreate(TarefaBase):
    usuarios_ids: List[int]


class TarefaUpdate(BaseModel):
    titulo: Optional[str]
    descricao: Optional[str]
    status: Optional[str]
    usuarios_ids: Optional[List[int]]


class TarefaOut(TarefaBase):
    id: int
    data_criacao: Optional[date]
    usuarios: List[int]  # IDs dos usuarios atribuidos

    class Config:
        orm_mode = True

# ---------- Usuario ----------
class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class Usuario_id(UsuarioBase):
    id: int

    class config:
        orm_mode = True

class UsuarioUpdate(BaseModel):
    nome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]


class UsuarioOut(BaseModel):
    id: int
    tarefas: List[int]  

    class Config:
        orm_mode = True