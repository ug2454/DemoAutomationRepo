import os
import requests

BASE_URL = os.environ.get("DEV_APP_URL", "http://127.0.0.1:8000")


def test_health():
    resp = requests.get(f"{BASE_URL}/health", timeout=5)
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_create_and_get_user():
    payload = {"name": "Ada", "email": "ada@example.com"}
    create = requests.post(f"{BASE_URL}/users", json=payload, timeout=5)
    assert create.status_code == 201
    body = create.json()
    assert body["name"] == "Ada"
    assert body["email"] == "ada@example.com"
    assert isinstance(body["id"], int)

    get_one = requests.get(f"{BASE_URL}/users/{body['id']}", timeout=5)
    assert get_one.status_code == 200
    assert get_one.json() == body


def test_list_users_contains_created_user():
    payload = {"name": "Grace", "email": "grace@example.com"}
    create = requests.post(f"{BASE_URL}/users", json=payload, timeout=5)
    assert create.status_code == 201
    created = create.json()

    list_resp = requests.get(f"{BASE_URL}/users", timeout=5)
    assert list_resp.status_code == 200
    users = list_resp.json()
    assert any(u["id"] == created["id"] for u in users)
