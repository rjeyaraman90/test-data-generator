import pytest
import responses
from src.record_inserter import RecordInserter


@responses.activate
def test_insert_records_success():
    # Mock Salesforce record creation response
    responses.add(
        responses.POST,
        "https://mock-instance.salesforce.com/services/data/v56.0/sobjects/Account/",
        json={"id": "mock_record_id", "success": True, "errors": []},
        status=201
    )

    inserter = RecordInserter("https://mock-instance.salesforce.com", "mock_access_token")
    records = [{"Name": "Test Account"}]
    inserter.insert_records("Account", records)

    assert len(responses.calls) == 1


@responses.activate
def test_insert_records_failure():
    # Mock Salesforce record creation failure response
    responses.add(
        responses.POST,
        "https://mock-instance.salesforce.com/services/data/v56.0/sobjects/Account/",
        json={"errors": [{"statusCode": "REQUIRED_FIELD_MISSING", "message": "Required fields are missing"}]},
        status=400
    )

    inserter = RecordInserter("https://mock-instance.salesforce.com", "mock_access_token")
    records = [{"Name": "Test Account"}]

    with pytest.raises(Exception) as exc_info:
        inserter.insert_records("Account", records)

    assert "Failed to insert record" in str(exc_info.value)
