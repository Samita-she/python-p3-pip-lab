from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_requests_version():
    assert requests_version() == "2.32.3"  # Adjust to the actual version installed or required

def test_pytest_version():
    assert pytest_version() == "8.3.5"  # Adjust to the actual version installed or required
