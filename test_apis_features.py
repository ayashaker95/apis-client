import pytest
import allure
import logging
from base_fixture import api_test
from base_fixture import sample_user

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@allure.feature("User Management")
class TestUsers:
    @allure.story("Retrieve all users")
    def test_get_all_users(self, api_test):
        response = api_test.get("/users")
        assert response.status_code == 200, "Expected status code 200"
        users = response.json()
        assert isinstance(users, list), "Expected a list of users"
        logging.info("Successfully retrieved all users")
    
    @allure.story("Validate user data structure")
    def test_validate_user_data_structure(self, api_test):
        response = api_test.get("/users/1")
        assert response.status_code == 200, "Expected status code 200"
        user = response.json()
        required_keys = {"id", "name", "username", "email", "address", "phone", "website", "company"}
        assert required_keys.issubset(user.keys()), "User data structure is incorrect"
        logging.info("User data structure validation passed")

    @allure.story("Create a user")
    def test_create_user(self, api_test, sample_user):
        response = api_test.post("/users", json=sample_user)
        assert response.status_code == 201, "Expected status code 201"
        created_user = response.json()
        assert created_user["name"] == sample_user["name"], "User name mismatch"
        logging.info("User successfully created")

@allure.feature("Post Management")
class TestPosts:
    @allure.story("Create a post")
    def test_create_post(self, api_test):
        payload = {
            "title": "Test Post",
            "body": "This is a test post.",
            "userId": 1
        }
        response = api_test.post("/posts", json=payload)
        assert response.status_code == 201, "Expected status code 201"
        logging.info("Post created successfully")
    
    @allure.story("Invalid post creation - missing fields")
    def test_create_post_missing_fields(self, api_test):
        payload = {"title": "Incomplete Post"}  # Missing 'body' and 'userId'
        response = api_test.post("/posts", json=payload)
        assert response.status_code == 400, "Expected status code 400"
        logging.warning("Post creation with missing fields correctly failed")

    @allure.story("Update a post")
    def test_update_post(self, api_test):
        response = api_test.get("/posts/1")
        post = response.json()
        updated_payload = {
            "title": "Updated Title",
            "body": post["body"],
            "userId": post["userId"]
        }
        update_response = api_test.put("/posts/1", json=updated_payload)
        assert update_response.status_code == 200, "Expected status code 200"
        logging.info("Post updated successfully")

    @allure.story("Delete a post")
    def test_delete_post(self, api_test):
        response = api_test.delete("/posts/1")
        assert response.status_code == 200, "Expected status code 200"
        logging.info("Post deleted successfully")

@allure.feature("Negative Testing")
class TestNegative:
    @allure.story("Invalid endpoint")
    def test_invalid_endpoint(self, api_test):
        response = api_test.get("/invalid_endpoint")
        assert response.status_code == 404, "Expected 404"
        logging.warning("Invalid endpoint correctly returned 404")

    @allure.story("Invalid data format")
    def test_invalid_data_format(self, api_test):
        response = api_test.post("/posts", json="invalid format")  # Sending string instead of JSON
        assert response.status_code == 400, "Expected 400 for invalid format"
        logging.warning("Invalid data format correctly returned 400")
