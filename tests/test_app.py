from app import app

def test_hello():
    with app.test_client() as client:
        response = client.get('/')
        # Fix: compare strings after decoding
        assert response.data.decode('utf-8') == "Hello World from Siyanbola Abraham! 🚀"
