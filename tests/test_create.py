"""
Test module for CREATE operations (POST requests).

This module validates that new users can be created successfully
via POST API calls. Tests verify response status codes and data.
"""

import pytest


class TestCreateOperations:
    """
    Test class for CREATE (POST) API operations.

    Tests cover scenarios for creating new users with the API.
    """

    # Endpoint for users resource
    USERS_ENDPOINT = "/users"

    def test_create_user_success(self, api_client, sample_user_data):
        """
        Test creating a new user with valid data.

        Purpose:
            Verify that POST /users creates a new user successfully.

        API Endpoint:
            POST https://jsonplaceholder.typicode.com/users

        Payload:
            - name: "Nitin Gawali"
            - username: "nitin123"
            - email: "nitin@test.com"
            - address: Object with street, city, zipcode
            - phone: "9876543210"

        Expected Result:
            - Status code: 201 (Created)
            - Response contains 'id' field
            - Response data matches request payload
        """
        # Send POST request to create user
        response = api_client.post(self.USERS_ENDPOINT, json=sample_user_data)

        # Validate status code - 201 means resource created
        assert response.status_code == 201, (
            f"Expected 201 Created, got {response.status_code}"
        )

        # Parse response JSON
        response_data = response.json()

        # Validate response contains 'id' (assigned by server)
        assert "id" in response_data, "Response should contain 'id' field"

        # Validate returned data matches sent data
        assert response_data["name"] == sample_user_data["name"]
        assert response_data["email"] == sample_user_data["email"]
        assert response_data["username"] == sample_user_data["username"]

    def test_create_user_minimal_data(self, api_client):
        """
        Test creating a user with minimal required data.

        Purpose:
            Verify API handles minimal payload (name only).

        API Endpoint:
            POST /users

        Payload:
            - name: "Minimal User"

        Expected Result:
            - Status code: 201 (Created)
            - Response contains generated id
        """
        # Minimal payload with only name
        minimal_data = {"name": "Minimal User"}

        # Send POST request
        response = api_client.post(self.USERS_ENDPOINT, json=minimal_data)

        # Validate status code
        assert response.status_code == 201

        # Validate response contains generated id
        response_data = response.json()
        assert "id" in response_data
        assert response_data["name"] == "Minimal User"

    def test_create_user_response_contains_id(self, api_client, sample_user_data):
        """
        Test that created user has auto-generated positive ID.

        Purpose:
            Verify the API assigns a valid ID to new users.

        API Endpoint:
            POST /users

        Expected Result:
            - Response includes 'id' field
            - ID is a positive integer
        """
        # Create user
        response = api_client.post(self.USERS_ENDPOINT, json=sample_user_data)
        response_data = response.json()

        # Validate ID is positive integer
        user_id = response_data["id"]
        assert isinstance(user_id, int), "ID should be integer"
        assert user_id > 0, "ID should be positive"
