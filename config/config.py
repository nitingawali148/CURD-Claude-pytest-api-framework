"""
Configuration module for API Automation Framework.

This module stores all configuration settings centrally.
Having a single config file makes it easy to update settings
without changing test code.
"""

# ============================================================================
# API Configuration
# ============================================================================

# Base URL for the API under test
# jsonplaceholder.typicode.com is a free fake REST API for testing
BASE_URL = "https://jsonplaceholder.typicode.com"

# Request timeout in seconds
# Prevents tests from hanging if API is unresponsive
TIMEOUT = 10

# ============================================================================
# HTTP Headers
# ============================================================================

# Default headers sent with every request
# Content-Type: application/json is required for JSON payloads
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# ============================================================================
# API Endpoints
# ============================================================================

# Dictionary of available endpoints
# Makes it easy to reference endpoints without hardcoding strings
ENDPOINTS = {
    "users": "/users",
    "posts": "/posts",
    "comments": "/comments"
}

# ============================================================================
# Report Configuration
# ============================================================================

# Directory where HTML reports are saved
REPORTS_DIR = "reports"

# Report filename format with timestamp
# Format: report_YYYY-MM-DD_HH-MM-SS.html
REPORT_FILENAME_FORMAT = "report_{timestamp}.html"
