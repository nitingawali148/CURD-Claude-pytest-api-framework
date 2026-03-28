"""
Test module for UPDATE operations (PUT requests).

This module validates that existing users can be updated
via PUT API calls. Tests verify complete resource replacement.
"""


class TestUpdateOperations:
    """
    Test class for UPDATE (PUT) API operations.

    Tests cover updating existing user resources.
    """

    # Endpoint for users resource
    USERS_ENDPOINT = "/users"

    def test_update_user_success(self, api_client, updated_user_data):
        """
        Test updating an existing user with valid data.

        Purpose:
            Verify PUT /users/1 updates the user successfully.

        API Endpoint:
            PUT https://jsonplaceholder.typicode.com/users/1

        Payload:
            - name: "Updated Name"
            - username: "updateduser"
            - email: "updated@example.com"
            - address: Updated address object
            - phone: "9999999999"

        Expected Result:
            - Status code: 200 (OK)
            - Response contains updated data
            - ID remains unchanged
        """
        user_id = 1

        # Send PUT request to update user
        response = api_client.put(
            f"{self.USERS_ENDPOINT}/{user_id}",
            json=updated_user_data
        )

        # Validate status code
        assert response.status_code == 200

        # Parse response
        response_data = response.json()

        # Validate ID is preserved
        assert response_data["id"] == user_id, "ID should not change"

        # Validate data was updated
        assert response_data["name"] == updated_user_data["name"]
        assert response_data["email"] == updated_user_data["email"]

    def test_update_user_structure(self, api_client, updated_user_data):
        """
        Test that update response has correct structure.

        Purpose:
            Verify PUT response contains all expected fields.

        API Endpoint:
            PUT /users/2

        Expected Result:
            - Response contains id, name, username, email
            - Response contains address and phone
        """
        user_id = 2

        # Send PUT request
        response = api_client.put(
            f"{self.USERS_ENDPOINT}/{user_id}",
            json=updated_user_data
        )

        response_data = response.json()

        # Validate expected fields exist
        expected_fields = ["id", "name", "username", "email", "address", "phone"]
        for field in expected_fields:
            assert field in response_data, f"Response should contain '{field}'"

    def test_update_user_partial_data(self, api_client):
        """
        Test updating a user with partial data.

        Purpose:
            Verify API handles partial PUT updates.

        API Endpoint:
            PUT /users/1

        Payload:
            - name: "Partially Updated Name"

        Expected Result:
            - Status code: 200 (OK)
            - Provided field is updated
        """
        partial_data = {"name": "Partially Updated Name"}

        response = api_client.put(f"{self.USERS_ENDPOINT}/1", json=partial_data)

        # Validate status code
        assert response.status_code == 200

        # Validate name was updated
        response_data = response.json()
        assert response_data["name"] == "Partially Updated Name"
