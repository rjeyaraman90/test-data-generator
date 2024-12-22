import requests

class SalesforceMetadata:
    """
        Fetches metadata for a specified Salesforce object.
    """
    def __init__(self, instance_url, token):
        """
                Initializes the class with the Salesforce instance URL and access token.

                Args:
                    instance_url (str): The base URL of the Salesforce instance.
                    token (str): The access token obtained after authentication.
        """
        self.instance_url = instance_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def fetch_metadata(self, object_name):
        """
                Fetches metadata for the specified Salesforce object.

                Args:
                    object_name (str): The Salesforce object name (e.g., "Account").

                Returns:
                    dict: Metadata information of the Salesforce object.

                Raises:
                    Exception: If the metadata request fails.
        """
        url = f"{self.instance_url}/services/data/v56.0/sobjects/{object_name}/describe"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch metadata: {response.json()}")
