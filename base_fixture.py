import pytest
from api_client import APIClient

@pytest.fixture
def api_test():
    return APIClient()

@pytest.fixture
def sample_user():
    return {
        "name": "Test User",
        "username": "testuser",
        "email": "testuser@example.com",
        "address": {"street": "123 Test St", "city": "Test City"},
        "phone": "123-456-7890",
        "website": "testuser.com",
        "company": {"name": "Test Company"}
    }


