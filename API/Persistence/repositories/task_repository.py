from sqlalchemy.orm import Session
from API.Model import models
from API.Model.schemas import TarefaCreate
from datetime import date


def criar_tarefa(db: Session, tarefa: TarefaCreate):
    usuarios = db.query(models.Usuario).filter(models.Usuario.id.in_(tarefa.usuarios_ids)).all()
    db_tarefa = models.Tarefa(
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        status=tarefa.status,
        usuarios=usuarios
    )
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa

def buscar_tarefa_por_titulo(db: Session, tarefa_titulo: str):
    return db.query(models.Tarefa).filter(models.Tarefa.titulo == tarefa_titulo).first()

def listar_tarefas_por_usuario(db: Session, usuario_id: int):
    return db.query(models.Tarefa).join(models.Tarefa.usuarios).filter(models.Usuario.id == usuario_id).all()

def atualizar_tarefa(db: Session, tarefa_id: int, dados: dict):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    for key, value in dados.items():
        setattr(tarefa, key, value)
    db.commit()
    return tarefa

def deletar_tarefa(db: Session, tarefa_id: int):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    db.delete(tarefa)
    db.commit()
