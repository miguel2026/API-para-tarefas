from sqlalchemy.orm import Session
from Model import models
from Model.schemas import UsuarioBase

def criar_usuario(db: Session, usuario: UsuarioBase):
    db_usuario = models.Usuario(**usuario.model_dump())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def buscar_usuario_por_email(db: Session, usuario_email: int):
    return db.query(models.Usuario).filter(models.Usuario.email == usuario_email).first()

def atualizar_usuario(db: Session, usuario_id: int, dados: dict):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    for key, value in dados.items():
        setattr(usuario, key, value)
    db.commit()
    return usuario

def deletar_usuario(db: Session, usuario_id: int):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    db.delete(usuario)
    db.commit()
