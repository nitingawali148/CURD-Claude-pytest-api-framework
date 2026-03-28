"""
Test module for DELETE operations (DELETE requests).

This module validates that users can be deleted successfully
via DELETE API calls. Tests verify deletion response.
"""


class TestDeleteOperations:
    """
    Test class for DELETE API operations.

    Tests cover deleting user resources.

    Note: jsonplaceholder.typicode.com is a fake API that simulates
    deletion. It returns 200 but doesn't actually delete data.
    """

    # Endpoint for users resource
    USERS_ENDPOINT = "/users"

    def test_delete_user_success(self, api_client):
        """
        Test deleting an existing user.

        Purpose:
            Verify DELETE /users/1 removes the user.

        API Endpoint:
            DELETE https://jsonplaceholder.typicode.com/users/1

        Expected Result:
            - Status code: 200 (OK)
            - Response is an empty object {}
        """
        user_id = 1

        # Send DELETE request
        response = api_client.delete(f"{self.USERS_ENDPOINT}/{user_id}")

        # Validate status code
        assert response.status_code == 200

        # Validate response is empty object
        response_data = response.json()
        assert response_data == {}, "Response should be empty object"

    def test_delete_user_returns_empty_object(self, api_client):
        """
        Test delete returns empty object (jsonplaceholder behavior).

        Purpose:
            Verify the specific response format from jsonplaceholder
            when deleting a resource.

        API Endpoint:
            DELETE /users/2

        Expected Result:
            - Response is exactly {}
        """
        response = api_client.delete(f"{self.USERS_ENDPOINT}/2")
        response_data = response.json()

        assert response_data == {}, "Expected empty dict {}"

    def test_delete_multiple_users(self, api_client):
        """
        Test deleting multiple different users.

        Purpose:
            Verify DELETE works for different user IDs.

        API Endpoints:
            DELETE /users/3
            DELETE /users/5
            DELETE /users/10

        Expected Result:
            - Each DELETE returns status 200
            - Each response is empty object {}
        """
        user_ids = [3, 5, 10]

        for user_id in user_ids:
            response = api_client.delete(f"{self.USERS_ENDPOINT}/{user_id}")

            # Validate deletion success
            assert response.status_code == 200, f"Failed to delete user {user_id}"

            # Validate empty response
            response_data = response.json()
            assert response_data == {}, f"Empty response expected for user {user_id}"

    def test_delete_response_time(self, api_client):
        """
        Test delete request completes in reasonable time.

        Purpose:
            Verify DELETE requests complete within timeout.

        API Endpoint:
            DELETE /users/1

        Expected Result:
            - Status code: 200
            - Response time under 5 seconds
        """
        import time

        start_time = time.time()

        response = api_client.delete(f"{self.USERS_ENDPOINT}/1")

        elapsed_time = time.time() - start_time

        # Validate response
        assert response.status_code == 200

        # Validate time taken
        assert elapsed_time < 5.0, f"Delete took {elapsed_time:.2f}s, too slow"
