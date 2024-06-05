import pytest
import allure
import json
@pytest.mark.xdist_group(name="API")
class TestAPI:

    @pytest.mark.parametrize("artist_name, expected_genre", [
        ("Drake", "Rap"),
        ("The Beatles", "British Invasion")
    ])
    @allure.feature('Search Artist')
    @allure.story('Enter the name of the singer to search and check if the singer has a certain genre')
    def test_artist_genre(self, api_client, artist_name, expected_genre):
        artist = api_client.get_artist(artist_name)
        genres = [genre.lower() for genre in artist["genres"]]
        assert expected_genre.lower() in genres, f"Expected {expected_genre} in {artist['genres']}"
        with allure.step(f"Asserting if {artist_name} has the genre as '{expected_genre}'"):
            assert expected_genre.lower() in genres, f"Expected {expected_genre} in {artist['genres']}"
        with allure.step('Attach API Response'):
            allure.attach(json.dumps(artist), name="API Response for artist",
                          attachment_type=allure.attachment_type.JSON)

    @pytest.mark.parametrize("artist_name, expected_song", [
        ("Drake", "One Dance"),
        ("The Beatles", "Here Comes The Sun - Remastered 2009")
    ])
    @allure.feature('Search Artist')
    @allure.story('Enter the name of the singer to search and check if the singer has a certain song')
    def test_artist_songs(self, api_client, artist_name, expected_song):
        artist = api_client.get_artist(artist_name)
        top_tracks = api_client.get_artist_top_tracks(artist["id"])
        song_names = [track["name"] for track in top_tracks]
        assert expected_song in song_names, f"Expected {expected_song} in {song_names}"
        with allure.step(f"Asserting if {artist_name} has the popular song as '{expected_song}'"):
            assert expected_song in song_names, f"Expected {expected_song} in {song_names}"
        with allure.step('Attach API Response'):
            allure.attach(json.dumps(artist), name="API Response for artist",
                          attachment_type=allure.attachment_type.JSON)
        with allure.step('Attach API Response'):
            allure.attach(json.dumps(top_tracks), name="API Response for top tracks",
                          attachment_type=allure.attachment_type.JSON)
