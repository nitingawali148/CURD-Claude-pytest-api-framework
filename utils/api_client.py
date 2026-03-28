"""
Reusable API Client module with logging support.

This module provides a wrapper around the requests library.
Features:
- Automatic JSON pretty-printing for debugging
- Consistent timeout and header handling
- Detailed request/response logging
"""

import json
import requests
from config.config import BASE_URL, TIMEOUT, DEFAULT_HEADERS


class APIClient:
    """
    Reusable HTTP client for making API requests.

    Provides methods for GET, POST, PUT, DELETE with:
    - Centralized configuration
    - Automatic JSON formatting for logging
    - Request/response capture for HTML reports
    """

    def __init__(self, base_url=None, timeout=None, headers=None):
        """
        Initialize the API client.

        Args:
            base_url: API base URL (default: from config)
            timeout: Request timeout in seconds (default: from config)
            headers: Default HTTP headers (default: from config)
        """
        self.base_url = base_url if base_url else BASE_URL
        self.timeout = timeout if timeout else TIMEOUT
        self.headers = headers if headers else DEFAULT_HEADERS.copy()

        # Store last request/response for reporting
        self.last_request = None
        self.last_response = None

    def _format_json(self, data):
        """
        Format data as pretty-printed JSON string.

        Args:
            data: Dictionary to format

        Returns:
            Pretty-printed JSON string with indentation
        """
        if data is None:
            return ""

        try:
            return json.dumps(data, indent=2, ensure_ascii=False)
        except (TypeError, ValueError):
            return str(data)

    def _log_request(self, method, url, payload=None):
        """
        Log the outgoing HTTP request details to console.

        Args:
            method: HTTP method (GET, POST, etc.)
            url: Full request URL
            payload: Request body (optional)
        """
        # Clear the stored request/response
        self.last_request = None
        self.last_response = None

        # Store for HTML report
        self.last_request = {
            "method": method,
            "url": url,
            "headers": self.headers,
            "payload": payload
        }

        # Print to console (ASCII only for Windows compatibility)
        print("\n" + "=" * 60)
        print(f"[REQUEST] {method} {url}")
        print("=" * 60)

        if payload:
            print(f"Payload:\n{self._format_json(payload)}")

    def _log_response(self, response):
        """
        Log the HTTP response details to console.

        Args:
            response: Response object from requests library
        """
        print("\n" + "=" * 60)
        print(f"[RESPONSE] Status: {response.status_code}")
        print("=" * 60)

        try:
            # Parse and pretty-print JSON response
            response_json = response.json()
            print(f"Body:\n{json.dumps(response_json, indent=2, ensure_ascii=False)}")

            # Store for HTML report
            self.last_response = {
                "status_code": response.status_code,
                "body": response_json,
                "headers": dict(response.headers)
            }
        except json.JSONDecodeError:
            # If not JSON, print raw text
            print(f"Body:\n{response.text}")

            self.last_response = {
                "status_code": response.status_code,
                "body": response.text,
                "headers": dict(response.headers)
            }

        print("=" * 60 + "\n")

    def get(self, endpoint, params=None):
        """
        Send a GET request to retrieve data.

        Args:
            endpoint: API endpoint path (e.g., /users)
            params: Query parameters as dictionary (optional)

        Returns:
            Response object from requests library
        """
        url = f"{self.base_url}{endpoint}"
        self._log_request("GET", url)

        response = requests.get(
            url=url,
            params=params,
            headers=self.headers,
            timeout=self.timeout
        )

        self._log_response(response)
        return response

    def post(self, endpoint, json=None):
        """
        Send a POST request to create a new resource.

        Args:
            endpoint: API endpoint path
            json: JSON payload as dictionary

        Returns:
            Response object from requests library
        """
        url = f"{self.base_url}{endpoint}"
        self._log_request("POST", url, json)

        response = requests.post(
            url=url,
            json=json,
            headers=self.headers,
            timeout=self.timeout
        )

        self._log_response(response)
        return response

    def put(self, endpoint, json=None):
        """
        Send a PUT request to update a resource completely.

        Args:
            endpoint: API endpoint path
            json: JSON payload as dictionary

        Returns:
            Response object from requests library
        """
        url = f"{self.base_url}{endpoint}"
        self._log_request("PUT", url, json)

        response = requests.put(
            url=url,
            json=json,
            headers=self.headers,
            timeout=self.timeout
        )

        self._log_response(response)
        return response

    def delete(self, endpoint):
        """
        Send a DELETE request to remove a resource.

        Args:
            endpoint: API endpoint path including resource ID

        Returns:
            Response object from requests library
        """
        url = f"{self.base_url}{endpoint}"
        self._log_request("DELETE", url)

        response = requests.delete(
            url=url,
            headers=self.headers,
            timeout=self.timeout
        )

        self._log_response(response)
        return response
