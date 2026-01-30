from ..app import app   # relative import from tests/ to root

def test_hello():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data.decode('utf-8') == "Hello World from Siyanbola Abraham! 🚀"
