import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from API.Presentation.routes import router 
from API.Workflow import services

api = FastAPI()
api.include_router(router)

client = TestClient(api)

@pytest.fixture(autouse=True)
def mock_services(monkeypatch):
    # Usuários
    monkeypatch.setattr(services, "criar_usuario", MagicMock())
    monkeypatch.setattr(services, "obter_usuario", MagicMock(return_value={"id":1,"nome": "João", "email": "joao@example.com", "senha": "senha123"}))
    monkeypatch.setattr(services, "atualizar_usuario", MagicMock())
    monkeypatch.setattr(services, "excluir_usuario", MagicMock())

    # Tarefas
    monkeypatch.setattr(services, "criar_tarefa", MagicMock())
    monkeypatch.setattr(services, "obter_tarefa", MagicMock(return_value={"id": 1, "titulo": "Fazer algo", "descricao": "Detalhes", "status": "pendente","usuarios": [1, 2],"data_criacao": "2023-10-01"}))
    monkeypatch.setattr(services, "listar_tarefas", MagicMock(return_value=[
        { "titulo": "Tarefa 1", "descricao": "A", "status": "pendente"},
        {"titulo": "Tarefa 2", "descricao": "B", "status": "feita"},
    ]))
    monkeypatch.setattr(services, "atualizar_tarefa", MagicMock())
    monkeypatch.setattr(services, "excluir_tarefa", MagicMock())

# Usuários

def test_create_user():
    payload = {"nome": "João", "email": "joao@example.com","senha": "senha123"}
    response = client.post("/users", json=payload)
    assert response.status_code == 200

def test_get_user():
    response = client.get("/users/1")
    print(response.json())
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_user():
    payload = {"nome": "João Atualizado", "email": "joao@novo.com","senha": "novaSenha123"}
    response = client.put("/users/1", json=payload)
    assert response.status_code == 200

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200

# Tarefas

def test_create_task():
    payload = {
        "titulo": "Nova Tarefa",
        "descricao": "Descrição aqui",
        "status": "pendente",
        "usuarios_ids": [1, 2]
    }
    response = client.post("/tasks", json=payload)
    assert response.status_code == 200

def test_get_task():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_list_tasks():
    response = client.get("/tasks?assignedTo=1")
    assert response.status_code == 200
    assert "tarefas" in response.json()

def test_update_task():
    payload = {"titulo": "Atualizada", "descricao": "Nova descrição", "status": "feita","usuarios_ids": [1, 2]}
    response = client.put("/tasks/1", json=payload)
    assert response.status_code == 200

def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code == 200
