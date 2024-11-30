from app import app
from config import test_env

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0", debug=test_env)
