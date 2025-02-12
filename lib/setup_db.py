from models.veterinarian import Veterinarian
from models.patient import Patient
from models import CONN  # Import the database connection

def setup_database():
    """Initialize database tables"""
    Veterinarian.create_table()
    Patient.create_table()
    print("Database tables created successfully.")

if __name__ == "__main__":
    setup_database()
    CONN.close()  # Close the connection when done
