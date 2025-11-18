import requests
from requests.auth import HTTPBasicAuth

class NetworkHelper:
    def __init__(self, base_url, username, password):
        self.base_url = base_url.rstrip("/") + "/"
        self.auth = HTTPBasicAuth(username, password) if username and password else None

    def get(self, endpoint="", params=None):
        url = self.base_url + endpoint.lstrip("/")
        response = requests.get(url, auth=self.auth, params=params)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            return response.text

    def post(self, endpoint="", data=None):
        url = self.base_url + endpoint.lstrip("/")
        response = requests.post(url, json=data, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint="", data=None):
        url = self.base_url + endpoint.lstrip("/")
        response = requests.put(url, json=data, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint=""):
        url = self.base_url + endpoint.lstrip("/")
        response = requests.delete(url, auth=self.auth)
        response.raise_for_status()
        return {"status": response.status_code, "text": response.text}

#api1
    def get_settlements(self):
        return self.get("settlements/")

    def get_settlement(self, pk):
        return self.get(f"settlements/{pk}/")

    def create_settlement(self, data):
        return self.post(f"settlements/", data)

    def update_settlement(self, pk, data):
        return self.put(f"settlements/{pk}/", data)

    def delete_settlement(self, pk):
        return self.delete(f"settlements/{pk}/")

#api2

    def get_persons(self):
        return self.get("people/")

    def get_person(self, pk):
        return self.get(f"people/{pk}/")

    def create_person(self, data):
        return self.post(f"people/", data)

    def update_person(self, pk, data):
        return self.put(f"people/{pk}/", data)

    def delete_person(self, pk):
        return self.delete(f"people/{pk}/")




