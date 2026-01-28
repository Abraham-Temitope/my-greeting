from app import app  # Assuming you update app.py to importable
def test_hello():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b"Hello World from Siyanbola Abraham! 🚀"
