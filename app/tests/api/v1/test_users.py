from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

from main import application
from database.session import get_db
from models.users import Base, User

# Create test database
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override the dependency
application.dependency_overrides[get_db] = override_get_db

client = TestClient(application)

@pytest.fixture(autouse=True)
def setup_database():
    # Create tables
    Base.metadata.create_all(bind=engine)
    yield
    # Clean up after test
    Base.metadata.drop_all(bind=engine)

def test_create_user():
    # Test creating a new user
    response = client.post(
        "/users",
        json={"name": "Test User", "age": 25}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test User"
    assert data["age"] == 25
    assert "id" in data

def test_create_duplicate_user():
    # Create first user
    client.post(
        "/users",
        json={"name": "Test User", "age": 25}
    )
    
    # Try to create duplicate user
    response = client.post(
        "/users",
        json={"name": "Test User", "age": 30}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "User already exist"

def test_get_users():
    # Create a test user first
    client.post(
        "/users",
        json={"name": "Test User", "age": 25}
    )
    
    # Test getting all users
    response = client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["name"] == "Test User"
    assert data[0]["age"] == 25 