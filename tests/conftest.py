"""
Pytest configuration and fixtures module.

This file contains:
1. Pytest hooks for HTML report customization
2. Shared fixtures for all test files
"""

import json
import pytest
from datetime import datetime
from utils.api_client import APIClient
from config.config import BASE_URL, DEFAULT_HEADERS


# =============================================================================
# Pytest Hooks for HTML Report Enhancement
# =============================================================================

def pytest_html_report_title(report):
    """
    Customize the HTML report title.
    """
    report.title = "API Automation Test Report"


def pytest_html_results_table_header(cells):
    """
    Customize the HTML report table header.
    Adds columns for test description and request/response details.
    """
    cells.insert(2, "<th>Description</th>")
    cells.insert(3, "<th>Request/Response</th>")


def pytest_html_results_table_row(report, cells):
    """
    Customize each row in the HTML report table.
    """
    # Add description
    description = getattr(report, "test_description", "No description")
    cells.insert(2, f"<td>{description}</td>")

    # Add request/response
    request_response = getattr(report, "request_response", "N/A")
    cells.insert(3, f"<td>{request_response}</td>")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture test execution details for HTML report.
    This hook runs after each test and captures request/response.
    """
    outcome = yield
    report = outcome.get_result()

    # Only process after the test call (not setup/teardown)
    if call.when == "call":
        # Capture test description from docstring
        if item.function.__doc__:
            docstring = " ".join(item.function.__doc__.split())
            report.test_description = docstring[:200] + "..." if len(docstring) > 200 else docstring
        else:
            report.test_description = item.nodeid

        # Get the API client instance from the test
        api_client = None
        if hasattr(item, "funcargs") and "api_client" in item.funcargs:
            api_client = item.funcargs["api_client"]

        if api_client and hasattr(api_client, "last_request") and api_client.last_request:
            # Format request details
            request = api_client.last_request
            payload_str = ""
            if request.get("payload"):
                payload_str = json.dumps(request["payload"], indent=2)

            request_html = f"""
            <div style="background-color: #e3f2fd; padding: 8px; margin: 4px 0; border-left: 3px solid #2196F3; font-size: 11px;">
                <b>REQUEST: {request['method']} {request['url']}</b><br/>
                <pre style="background-color: #fff; padding: 4px; margin: 4px 0;">{payload_str if payload_str else 'No Payload'}</pre>
            </div>
            """

            # Format response details
            if hasattr(api_client, "last_response") and api_client.last_response:
                response = api_client.last_response
                body = response.get("body", "")
                if isinstance(body, (dict, list)):
                    body_str = json.dumps(body, indent=2, ensure_ascii=False)
                else:
                    body_str = str(body)

                response_html = f"""
                <div style="background-color: #e8f5e9; padding: 8px; margin: 4px 0; border-left: 3px solid #4CAF50; font-size: 11px;">
                    <b>RESPONSE: {response['status_code']}</b><br/>
                    <pre style="background-color: #fff; padding: 4px; margin: 4px 0;">{body_str}</pre>
                </div>
                """
            else:
                response_html = "<div>No response</div>"

            report.request_response = request_html + response_html
        else:
            report.request_response = "<div>No API call</div>"


# =============================================================================
# Pytest Fixtures
# =============================================================================

@pytest.fixture(scope="session")
def api_client():
    """
    Fixture to provide a reusable API client instance.

    This fixture creates an APIClient that is shared across all tests
    in the session. Session scope means it's created once and reused.
    """
    client = APIClient(base_url=BASE_URL, headers=DEFAULT_HEADERS.copy())
    return client


@pytest.fixture(scope="module")
def test_headers():
    """
    Fixture to provide default HTTP headers.
    """
    return DEFAULT_HEADERS.copy()


@pytest.fixture(scope="module")
def sample_user_data():
    """
    Fixture to provide sample user data for CREATE operations.
    """
    return {
        "name": "Nitin Gawali",
        "username": "nitin123",
        "email": "nitin@test.com",
        "address": {
            "street": "ABC Street",
            "city": "Pune",
            "zipcode": "411001"
        },
        "phone": "9876543210"
    }


@pytest.fixture(scope="module")
def updated_user_data():
    """
    Fixture to provide updated user data for UPDATE operations.
    """
    return {
        "name": "Updated Name",
        "username": "updateduser",
        "email": "updated@example.com",
        "address": {
            "street": "Updated Street",
            "city": "Mumbai",
            "zipcode": "400001"
        },
        "phone": "9999999999"
    }
