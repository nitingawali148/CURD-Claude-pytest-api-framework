# API Automation Framework

A clean, scalable Python + pytest framework for CRUD API testing with detailed HTML reporting.

## Project Structure

```
CURD_API Automation/
├── config/                    # Configuration files
│   ├── __init__.py
│   └── config.py              # Base URL, timeout, headers
├── utils/                     # Utility modules
│   ├── __init__.py
│   └── api_client.py          # Reusable HTTP client with logging
├── tests/                     # Test files
│   ├── __init__.py
│   ├── conftest.py            # Pytest fixtures & HTML report hooks
│   ├── test_create.py         # POST tests (Create)
│   ├── test_read.py           # GET tests (Read)
│   ├── test_update.py         # PUT tests (Update)
│   └── test_delete.py         # DELETE tests (Delete)
├── reports/                   # HTML test reports (auto-generated)
├── run_tests.py               # Test runner with timestamped reports
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Features

- ✅ **CRUD Operations**: Complete test coverage for Create, Read, Update, Delete
- ✅ **Reusable API Client**: Centralized HTTP handling with logging
- ✅ **Pretty JSON Logging**: Request/response displayed in console
- ✅ **Enhanced HTML Reports**: Includes request details, response data, descriptions
- ✅ **Timestamped Reports**: Report filenames include date and time
- ✅ **Detailed Comments**: Every file has clear documentation
- ✅ **Scalable Structure**: Easy to add new tests

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Tests

#### Option A: Using the run script (recommended)
```bash
python run_tests.py
```
This generates: `reports/report_2026-03-28_14-30-25.html`

#### Option B: Run with manual timestamp
```bash
pytest --html=reports/report_$(date +%%Y-%%m-%%d_%%H-%%M-%%S).html --self-contained-html -v -s
```

#### Option C: Run all tests with verbose output
```bash
pytest -v -s
```

#### Option D: Run specific test file
```bash
pytest tests/test_create.py -v -s
```

## Test Coverage

| Operation | File | Method | Tests |
|-----------|------|--------|-------|
| Create | `test_create.py` | POST | 3 |
| Read | `test_read.py` | GET | 4 |
| Update | `test_update.py` | PUT | 3 |
| Delete | `test_delete.py` | DELETE | 4 |
| **Total** | | | **14** |

## API Under Test

- **URL**: https://jsonplaceholder.typicode.com
- **Type**: Free fake REST API
- **Resources**: Users, Posts, Comments
- **Features**: Simulates real API behavior

## Report Features

Each HTML report includes:

1. **Test Summary**: Pass/fail count with timestamps
2. **Test Description**: Extracted from docstrings
3. **Request Details**:
   - HTTP method and URL
   - Headers
   - Request payload (pretty JSON)
4. **Response Details**:
   - Status code
   - Response body (pretty JSON)

## Console Output

When running tests, you'll see pretty-printed JSON:

```
============================================================
📤 REQUEST: POST https://jsonplaceholder.typicode.com/users
============================================================
Headers: {
  "Content-Type": "application/json",
  "Accept": "application/json"
}

Payload:
{
  "name": "Nitin Gawali",
  "username": "nitin123",
  ...
}

============================================================
📥 RESPONSE: Status 201
============================================================
Body:
{
  "id": 11,
  "name": "Nitin Gawali",
  ...
}
============================================================
```

## Customization

### Add New Tests
1. Create test method in appropriate `test_*.py` file
2. Use `api_client` fixture for HTTP requests
3. Add docstring explaining the test purpose
4. Assert on status codes and response data

### Modify Configuration
Edit `config/config.py`:
```python
BASE_URL = "https://your-api.com"
TIMEOUT = 30
```

## Requirements

- Python 3.8+
- pytest
- requests
- pytest-html

## License

This project is for educational and testing purposes.
