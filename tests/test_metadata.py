import pytest
import responses
from src.metadata import SalesforceMetadata


@responses.activate
def test_fetch_metadata_success():
    # Mock metadata response
    responses.add(
        responses.GET,
        "https://mock-instance.salesforce.com/services/data/v56.0/sobjects/Account/describe",
        json={"fields": [{"name": "Name", "type": "string"}, {"name": "Phone", "type": "string"}]},
        status=200
    )

    metadata = SalesforceMetadata("https://mock-instance.salesforce.com", "mock_access_token")
    fields = metadata.fetch_metadata("Account")

    assert fields["fields"][0]["name"] == "Name"
    assert fields["fields"][1]["type"] == "string"


@responses.activate
def test_fetch_metadata_failure():
    # Mock failed metadata response
    responses.add(
        responses.GET,
        "https://mock-instance.salesforce.com/services/data/v56.0/sobjects/Account/describe",
        status=404
    )

    metadata = SalesforceMetadata("https://mock-instance.salesforce.com", "mock_access_token")
    with pytest.raises(Exception) as exc_info:
        metadata.fetch_metadata("Account")

    assert "Failed to fetch metadata" in str(exc_info.value)
