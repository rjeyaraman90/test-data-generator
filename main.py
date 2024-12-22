from src.auth import SalesforceAuth
from src.metadata import SalesforceMetadata
from src.data_generator import DataGenerator

def main():
    # Step 1: Authenticate with Salesforce
    print("Authenticating with Salesforce...")
    try:
        auth = SalesforceAuth()
        token, instance_url = auth.authenticate()
        print(f"Access Token: {token}")
        print(f"Instance URL: {instance_url}")
    except Exception as e:
        print(f"Error during authentication: {e}")
        return

    # Step 2: Fetch metadata for a specified object
    object_name = "Account"
    print(f"Fetching metadata for Salesforce object: {object_name}...")
    try:
        metadata = SalesforceMetadata(instance_url, token)
        object_metadata = metadata.fetch_metadata(object_name)
        print(f"Raw Metadata for {object_name}: {object_metadata}")  # Debugging line
        # Parse fields safely
        fields = {}
        if "fields" in object_metadata and isinstance(object_metadata["fields"], list):
            fields = {field["name"]: field["type"] for field in object_metadata["fields"] if
                      "name" in field and "type" in field}
        else:
            print("Error: Fields metadata is missing or malformed.")
            return

        print(f"Fields for {object_name}: {fields}")
    except Exception as e:
        print(f"Error fetching metadata: {e}")
        return

    # Step 3: Generate test data
    record_count = 5  # Number of records to generate
    print(f"Generating {record_count} test records for {object_name}...")
    try:
        data_gen = DataGenerator()
        fake_data = data_gen.generate_data(fields, record_count)
        print("Generated Data:")
        for record in fake_data:
            print(record)
    except Exception as e:
        print(f"Error generating test data: {e}")

if __name__ == "__main__":
    main()
