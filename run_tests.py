"""
Test Runner Script with Timestamped Reports.

This script runs pytest and generates HTML reports with date/time in filename.

Usage:
    python run_tests.py

Output:
    - Console output with pretty-printed JSON
    - HTML report in reports/ folder (e.g., report_2026-03-28_14-30-25.html)
"""

import subprocess
import sys
from datetime import datetime


def get_timestamped_filename():
    """
    Generate report filename with current timestamp.

    Format: report_YYYY-MM-DD_HH-MM-SS.html
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"reports/report_{timestamp}.html"


def main():
    """
    Main function to run tests with HTML report.
    """
    # Generate timestamped report filename
    report_file = get_timestamped_filename()

    print("=" * 60)
    print("API Automation Test Runner")
    print("=" * 60)
    print(f"Report will be saved to: {report_file}")
    print("=" * 60)

    # Build pytest command
    pytest_args = [
        "pytest",
        "--html=" + report_file,
        "--self-contained-html",
        "-v",
        "-s",
    ]

    # Run pytest
    result = subprocess.run(pytest_args, cwd=".")

    print("\n" + "=" * 60)
    if result.returncode == 0:
        print("SUCCESS: All tests passed!")
    else:
        print("FAILED: Some tests failed!")
    print(f"Report saved: {report_file}")
    print("=" * 60)

    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
