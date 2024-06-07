import allure
import requests
from requests.auth import HTTPBasicAuth
from config import CLIENT_ID, CLIENT_SECRET, BASE_API_URL, TOKEN_URL

class SpotifyClient:
    def __init__(self):
        self.token = self.__get_access_token(self)
    @staticmethod
    @allure.step("Getting access token")
    def __get_access_token(self):
        response = requests.post(
            TOKEN_URL,
            data={"grant_type": "client_credentials"},
            auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
        )
        if response.status_code != 200:
            allure.attach(response.text, name="Token Error Response", attachment_type=allure.attachment_type.TEXT)
            raise ConnectionError("Failed to authenticate with Spotify API")
        return response.json()["access_token"]

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    @allure.step("Getting artist information for {artist_name}")
    def get_artist(self, artist_name):
        response = requests.get(
            f"{BASE_API_URL}/search",
            headers=self.get_headers(),
            params={"q": artist_name, "type": "artist"}
        )
        if response.status_code != 200:
            allure.attach(response.text, name="Artist Error Response", attachment_type=allure.attachment_type.TEXT)
            raise ConnectionError("Failed to get artist data!")
        artist_data = response.json()["artists"]["items"][0]
        allure.attach(str(artist_data), name="Artist Data", attachment_type=allure.attachment_type.JSON)
        return artist_data

    @allure.step("Getting top tracks for artist ID {artist_id}")
    def get_artist_top_tracks(self, artist_id):
        response = requests.get(
            f"{BASE_API_URL}/artists/{artist_id}/top-tracks",
            headers=self.get_headers(),
            params={"market": "US"} # should return results tailored to the US market.
        )
        if response.status_code != 200:
            allure.attach(response.text, name="Tracks Error Response", attachment_type=allure.attachment_type.TEXT)
            raise ConnectionError("Failed to get artist's tracks data!")
        tracks = response.json()["tracks"]
        allure.attach(str(tracks), name="Top Tracks", attachment_type=allure.attachment_type.JSON)
        return tracks
