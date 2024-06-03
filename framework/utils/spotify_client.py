import requests
from requests.auth import HTTPBasicAuth
from config import CLIENT_ID, CLIENT_SECRET, BASE_API_URL, TOKEN_URL

class SpotifyClient:
    def __init__(self):
        self.token = self.__get_access_token(self)
    @staticmethod
    def __get_access_token(self):
        response = requests.post(
            TOKEN_URL,
            data={"grant_type": "client_credentials"},
            auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
        )
        if response.status_code != 200:
            raise ConnectionError("Failed to authenticate with Spotify API")
        return response.json()["access_token"]

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    def get_artist(self, artist_name):
        response = requests.get(
            f"{BASE_API_URL}/search",
            headers=self.get_headers(),
            params={"q": artist_name, "type": "artist"}
        )
        if response.status_code != 200:
            raise ConnectionError("Failed to get artist data!")
        return response.json()["artists"]["items"][0] # retrieves the first searched name

    def get_artist_top_tracks(self, artist_id):
        response = requests.get(
            f"{BASE_API_URL}/artists/{artist_id}/top-tracks",
            headers=self.get_headers(),
            params={"market": "US"} # should return results tailored to the US market.
        )
        if response.status_code != 200:
            raise ConnectionError("Failed to get artists' tracks data!")
        return response.json()["tracks"]
