from fastapi import APIRouter
from Workflow import services
from Model import models, schemas
from Persistence import database
from Persistence.repositories import user_repository, task_repository 

session = database.SessionLocal
router = APIRouter()

# Usuários

@router.post("/users")
async def create_user(usuario: schemas.UsuarioBase):
    """
    Cria um novo usuário.
    """
    services.criar_usuario(session, schemas.UsuarioBase)

@router.get("/users/{id}",response_model=schemas.UsuarioBase)
async def get_user(id: int):
    """
    Obtém informações de um usuário específico.
    """
    return services.obter_usuario(session, id)

@router.put("/users/{id}")
async def update_user(id: int, usuario: schemas.UsuarioUpdate):
    """
    Atualiza informações do usuário.
    """
    services.atualizar_usuario(session, id, usuario.model_dump())
    

@router.delete("/users/{id}")
async def delete_user(id: int):
    """
    Remove um usuário com soft delete.
    """
    services.excluir_usuario(session, id)

# Tarefas

@router.post("/tasks")
async def create_task(tarefa: schemas.TarefaCreate):
    """
    Cria uma nova tarefa. é necessário fornecer a lista de IDs dos usuários atribuídos à tarefa.
    """
    services.criar_tarefa(session, tarefa)

@router.get("/tasks/{id}",response_model=schemas.TarefaOut)
async def get_task(id: int):
    """
    Obtém detalhes de uma tarefa.
    """
    return services.obter_tarefa(session, id)

@router.get("/tasks",response_model=schemas.UsuarioOut)
async def list_tasks(assignedTo: int = None):
    """
    Lista todas as tarefas atribuídas a um usuário específico.
    """
    if assignedTo:
        return schemas.UsuarioOut(id=assignedTo, tarefas=services.listar_tarefas(session, assignedTo))

@router.put("/tasks/{id}")
async def update_task(id: int, Tarefa: schemas.TarefaUpdate):
    """
    Atualiza informações de uma tarefa (título, descrição, status).
    """
    services.atualizar_tarefa(session, id, Tarefa.model_dump())

@router.delete("/tasks/{id}")
async def delete_task(id: int):
    """
    Remove uma tarefa.
    """
    services.excluir_tarefa(session, id)

# autenticação

@router.post("/auth/login")
async def login():
    """
    Login de usuários, retornando um token para autenticação nas demais requisições.
    """
    return {"message": "Login realizado com sucesso."}

@router.post("/auth/logout")
async def logout():
    """
    Logout do usuário.
    """
    return {"message": "Logout realizado com sucesso."}