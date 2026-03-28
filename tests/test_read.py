"""
Test module for READ operations (GET requests).

This module validates that users can be retrieved successfully
via GET API calls. Tests cover listing all users and fetching
individual users by ID.
"""


class TestReadOperations:
    """
    Test class for READ (GET) API operations.

    Tests cover retrieving single users and user lists.
    """

    # Endpoint for users resource
    USERS_ENDPOINT = "/users"

    def test_get_all_users(self, api_client):
        """
        Test retrieving all users from the API.

        Purpose:
            Verify GET /users returns a list of all users.

        API Endpoint:
            GET https://jsonplaceholder.typicode.com/users

        Expected Result:
            - Status code: 200 (OK)
            - Response is a list
            - List contains at least one user
            - Each user has required fields (id, name, email)
        """
        # Send GET request
        response = api_client.get(self.USERS_ENDPOINT)

        # Validate status code
        assert response.status_code == 200

        # Parse response
        response_data = response.json()

        # Validate response is a list
        assert isinstance(response_data, list), "Response should be a list"

        # Validate list is not empty
        assert len(response_data) > 0, "Users list should not be empty"

        # Validate each user has required fields
        for user in response_data:
            assert "id" in user, "User should have 'id'"
            assert "name" in user, "User should have 'name'"
            assert "email" in user, "User should have 'email'"

    def test_get_user_by_id(self, api_client):
        """
        Test retrieving a specific user by ID.

        Purpose:
            Verify GET /users/1 returns the correct user.

        API Endpoint:
            GET https://jsonplaceholder.typicode.com/users/1

        Expected Result:
            - Status code: 200 (OK)
            - Response is a single user object
            - User ID matches request (1)
            - User has name, email, and username
        """
        test_user_id = 1

        # Send GET request for specific user
        response = api_client.get(f"{self.USERS_ENDPOINT}/{test_user_id}")

        # Validate status code
        assert response.status_code == 200

        # Parse response
        response_data = response.json()

        # Validate response is a dictionary (single user)
        assert isinstance(response_data, dict), "Response should be an object"

        # Validate user ID matches
        assert response_data["id"] == test_user_id

        # Validate required fields exist
        assert response_data["name"], "User should have a name"
        assert response_data["email"], "User should have an email"
        assert response_data["username"], "User should have a username"

    def test_get_user_has_address(self, api_client):
        """
        Test that user data includes nested address.

        Purpose:
            Verify user response contains complete address data.

        API Endpoint:
            GET /users/1

        Expected Result:
            - Response includes 'address' object
            - Address contains street, city, zipcode
        """
        response = api_client.get(f"{self.USERS_ENDPOINT}/1")
        user = response.json()

        # Validate address structure
        assert "address" in user, "User should have address"

        address = user["address"]
        assert "street" in address, "Address should have street"
        assert "city" in address, "Address should have city"
        assert "zipcode" in address, "Address should have zipcode"

    def test_get_user_has_contact_info(self, api_client):
        """
        Test that user includes contact information.

        Purpose:
            Verify user has phone, website, and company info.

        API Endpoint:
            GET /users/1

        Expected Result:
            - Response includes phone number
            - Response includes website
            - Response includes company object
        """
        response = api_client.get(f"{self.USERS_ENDPOINT}/1")
        user = response.json()

        # Validate contact info exists
        assert "phone" in user and user["phone"], "Should have phone"
        assert "website" in user and user["website"], "Should have website"
        assert "company" in user, "Should have company info"
