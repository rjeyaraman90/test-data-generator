from src.auth import SalesforceAuth
from src.metadata import SalesforceMetadata
from src.data_generator import DataGenerator
from src.record_inserter import RecordInserter
from src.cli import CLI

def main():
    # Step 1: Parse Command-Line Arguments
    args = CLI.parse_arguments()
    object_name = args.object
    record_count = args.record_count
    verbose = args.verbose

    if verbose:
        print(f"Arguments received: object={object_name}, record_count={record_count}, verbose={verbose}")

    # Step 2: Authenticate with Salesforce
    print("Authenticating with Salesforce...")
    auth = SalesforceAuth()
    try:
        token, instance_url = auth.authenticate()
    except Exception as e:
        print(f"Authentication failed: {e}")
        return

    if verbose:
        print(f"Authenticated successfully. Token: {token}, Instance URL: {instance_url}")

    # Step 3: Fetch Metadata for the Target Object
    print(f"Fetching metadata for Salesforce object: {object_name}...")
    metadata = SalesforceMetadata(instance_url, token)
    try:
        object_metadata = metadata.fetch_metadata(object_name)
    except Exception as e:
        print(f"Failed to fetch metadata: {e}")
        return

    # Parse field information from metadata
    fields = {field["name"]: field["type"] for field in object_metadata["fields"]}
    if verbose:
        print(f"Fetched fields: {fields}")

    # Step 4: Generate Fake Data
    print(f"Generating {record_count} fake records for {object_name}...")
    data_gen = DataGenerator()
    fake_data = data_gen.generate_data(fields, record_count)
    if verbose:
        print(f"Generated data: {fake_data}")

    # Step 5: Insert Records into Salesforce
    print(f"Inserting records into Salesforce object: {object_name}...")
    inserter = RecordInserter(instance_url, token)
    try:
        inserter.insert_records(object_name, fake_data)
    except Exception as e:
        print(f"Failed to insert records: {e}")
        return

    print("Records successfully inserted into Salesforce!")

if __name__ == "__main__":
    main()
