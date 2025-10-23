import json
import pytest
import requests


def test_create_user(api_client):
    with open("test_data.json") as f:
        data = json.load(f)

    endpoint = "public/v2/users"
    response = api_client.post(endpoint, data)

    assert response.status_code == 201
    user_id = response.json()["id"]
    print(f" User created successfully with ID: {user_id}")

    
    return user_id


def test_update_user(api_client):
    user_id = 8184625 
    endpoint = f"public/v2/users/{user_id}"

    updated_data = {
        "name": "Samiul Updated",
        "status": "inactive"
    }

    response = api_client.put(endpoint, updated_data)
    assert response.status_code == 200
    print(" User updated successfully!")


def test_delete_user(api_client):
    user_id = 8184625  
    endpoint = f"public/v2/users/{user_id}"

    response = api_client.delete(endpoint)
    assert response.status_code == 204
    print(" User deleted successfully!")


print("Tests for creating, updating, and deleting a user have been defined.")
print ("feat-b")
print("bug/log 1")
print("bug/log 2")
