from fastapi import APIRouter
from Workflow.models import Criar_usuario, Criar_tarefa
router = APIRouter()

# Usuários

@router.post("/users")
async def create_user():
    """
    Cria um novo usuário.
    """
    return {"message": "Usuário criado com sucesso.",
            "id": Criar_usuario()}

@router.get("/users/{id}")
async def get_user(id: int):
    """
    Obtém informações de um usuário específico.
    """
    return {"message": f"Informações do usuário {id} obtidas com sucesso."}

@router.put("/users/{id}")
async def update_user(id: int):
    """
    Atualiza informações do usuário.
    """
    return {"message": f"Usuário {id} atualizado com sucesso."}

@router.delete("/users/{id}")
async def delete_user(id: int):
    """
    Remove um usuário com soft delete.
    """
    return {"message": f"Usuário {id} removido com sucesso."}

# Tarefas

@router.post("/tasks")
async def create_task():
    """
    Cria uma nova tarefa.
    """
    return {"message": "Tarefa criada com sucesso.",
            "id": Criar_tarefa()}

@router.get("/tasks/{id}")
async def get_task(id: int):
    """
    Obtém detalhes de uma tarefa.
    """
    return {"message": f"Detalhes da tarefa {id} obtidos com sucesso."}

@router.get("/tasks")
async def list_tasks(assignedTo: int = None):
    """
    Lista todas as tarefas atribuídas a um usuário específico.
    """
    if assignedTo:
        return {"message": f"Tarefas atribuídas ao usuário {assignedTo} obtidas com sucesso."}
    return {"message": "Todas as tarefas obtidas com sucesso."}

@router.put("/tasks/{id}")
async def update_task(id: int):
    """
    Atualiza informações de uma tarefa (título, descrição, status).
    """
    return {"message": f"Tarefa {id} atualizada com sucesso."}

@router.delete("/tasks/{id}")
async def delete_task(id: int):
    """
    Remove uma tarefa.
    """
    return {"message": f"Tarefa {id} removida com sucesso."}

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