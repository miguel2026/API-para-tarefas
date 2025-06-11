import pydantic
from API.Persistence.repositories import user_repository,task_repository
from sqlalchemy.orm import Session
from API.Model import schemas

def criar_usuario(db: Session, usuario: schemas.UsuarioBase):
    # Regras de negócio (ex: impedir emails duplicados)
    existente = user_repository.buscar_usuario_por_email(db, usuario.email)
    if existente:
        raise ValueError("Usuário com esse e-mail já existe")
    
    return user_repository.criar_usuario(db, usuario)

def obter_usuario(db: Session, usuario_id: int):
    usuario = user_repository.buscar_usuario_por_id(db, usuario_id)
    if not usuario:
        raise ValueError("Usuário não encontrado")
    return usuario

def atualizar_usuario(db: Session, usuario_id: int, dados: dict):
    usuario = user_repository.buscar_usuario_por_id(db, usuario_id)
    if not usuario:
        raise ValueError("Usuário não encontrado")

    return user_repository.atualizar_usuario(db, usuario_id, dados)

def excluir_usuario(db: Session, usuario_id: int):
    usuario = user_repository.buscar_usuario_por_id(db, usuario_id)
    if not usuario:
        raise ValueError("Usuário não encontrado")
    
    user_repository.deletar_usuario(db, usuario_id)

def criar_tarefa(db: Session, tarefa: schemas.TarefaCreate):
    existente = task_repository.buscar_tarefa_por_titulo(db, tarefa.titulo)
    if existente:
        raise ValueError("Tarefa com esse título já existe")
    
    return task_repository.criar_tarefa(db, tarefa)

def obter_tarefa(db: Session, tarefa_id: int):
    tarefa = task_repository.buscar_tarefa_por_id(db, tarefa_id)
    if not tarefa:
        raise ValueError("Tarefa não encontrada")
    return tarefa
def listar_tarefas(db: Session, usuario_id: int = None):
    if usuario_id:
        return task_repository.listar_tarefas_por_usuario(db, usuario_id)
    return None
def atualizar_tarefa(db: Session, tarefa_id: int, dados: schemas.TarefaUpdate):
    tarefa = task_repository.buscar_tarefa_por_id(db, tarefa_id)
    if not tarefa:
        raise ValueError("Tarefa não encontrada")
    
    return task_repository.atualizar_tarefa(db, tarefa_id, dados.model_dump())

def excluir_tarefa(db: Session, tarefa_id: int):
    tarefa = task_repository.buscar_tarefa_por_id(db, tarefa_id)
    if not tarefa:
        raise ValueError("Tarefa não encontrada")
    
    task_repository.deletar_tarefa(db, tarefa_id)