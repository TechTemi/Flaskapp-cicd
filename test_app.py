from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

    data = response.get_json()
    assert data["message"] == "Hello from Flask on EC2!"
    assert data["status"] == "running"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "healthy"


def test_add():
    client = app.test_client()
    response = client.get("/add/5/3")
    assert response.status_code == 200

    data = response.get_json()
    assert data["a"] == 5
    assert data["b"] == 3
    assert data["result"] == 8
