import requests

class SalesforceMetadata:
    def __init__(self, instance_url, token):
        self.instance_url = instance_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def fetch_metadata(self, object_name):
        url = f"{self.instance_url}/services/data/v56.0/sobjects/{object_name}/describe"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch metadata: {response.json()}")
