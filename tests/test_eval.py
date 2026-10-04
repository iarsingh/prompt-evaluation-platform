from fastapi.testclient import TestClient
from prompteval.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/evaluate", json={"answer": 'Refuse latest tags in production.', "gold": 'Refuse latest tags in production.', "context": 'The platform refuses latest tags in production.'}).json()
    assert good["passed"] is True
    bad = client.post("/evaluate", json={"answer": "The cafeteria serves soup.", "gold": 'Refuse latest tags in production.', "context": 'The platform refuses latest tags in production.'}).json()
    assert bad["passed"] is False
