import os
import requests
from dotenv import load_dotenv

class SalesforceAuth:
    def __init__(self):
        load_dotenv(dotenv_path="access.env")
        self.client_id = os.getenv("SF_CLIENT_ID")
        self.client_secret = os.getenv("SF_CLIENT_SECRET")
        self.username = os.getenv("SF_USERNAME")
        self.password = os.getenv("SF_PASSWORD")
        self.login_url = os.getenv("SF_LOGIN_URL")

    def authenticate(self):
        payload = {
            "grant_type": "password",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "username": self.username,
            "password": self.password,
        }
        response = requests.post(f"{self.login_url}/services/oauth2/token", data=payload)
        if response.status_code == 200:
            auth_data = response.json()
            return auth_data["access_token"], auth_data["instance_url"]
        else:
            raise Exception(f"Authentication failed: {response.json()}")
