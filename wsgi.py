# wsgi.py
from app import app as application  # Import the 'app' object from app.py

if __name__ == "__main__":
    application.run()