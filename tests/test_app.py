import sys
import os

# Add project root to Python path so 'app' is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_hello():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data.decode('utf-8') == "Hello World from Siyanbola Abraham! 🚀"

