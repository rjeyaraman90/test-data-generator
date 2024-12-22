import requests

class RecordInserter:
    def __init__(self, instance_url, token):
        self.instance_url = instance_url
        self.headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    def insert_records(self, object_name, records):
        url = f"{self.instance_url}/services/data/v56.0/sobjects/{object_name}/"
        for record in records:
            response = requests.post(url, headers=self.headers, json=record)
            if response.status_code not in [200, 201]:
                print(f"Failed to insert record: {response.json()}")
