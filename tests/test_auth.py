import pytest
import responses
from src.auth import SalesforceAuth


@responses.activate
def test_authenticate_success():
    # Mock Salesforce authentication response
    responses.add(
        responses.POST,
        "https://login.salesforce.com/services/oauth2/token",
        json={"access_token": "mock_access_token", "instance_url": "https://mock-instance.salesforce.com"},
        status=200
    )

    auth = SalesforceAuth()
    token, instance_url = auth.authenticate()

    assert token == "mock_access_token"
    assert instance_url == "https://mock-instance.salesforce.com"


@responses.activate
def test_authenticate_failure():
    # Mock failed authentication response
    responses.add(
        responses.POST,
        "https://login.salesforce.com/services/oauth2/token",
        json={"error": "invalid_grant", "error_description": "authentication failure"},
        status=400
    )

    auth = SalesforceAuth()
    with pytest.raises(Exception) as exc_info:
        auth.authenticate()

    assert "Authentication failed" in str(exc_info.value)
