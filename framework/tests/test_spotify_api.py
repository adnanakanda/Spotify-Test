import pytest

@pytest.mark.xdist_group(name="API")
class TestAPI:

    @pytest.mark.parametrize("artist_name, expected_genre", [
        ("Drake", "Rap"),
        ("The Beatles", "British Invasion")
    ])
    def test_artist_genre(self, api_client, artist_name, expected_genre):
        artist = api_client.get_artist(artist_name)
        genres = [genre.lower() for genre in artist["genres"]]
        assert expected_genre.lower() in genres, f"Expected {expected_genre} in {artist['genres']}"

    @pytest.mark.parametrize("artist_name, expected_song", [
        ("Drake", "One Dance"),
        ("The Beatles", "Here Comes The Sun - Remastered 2009")
    ])
    def test_artist_songs(self, api_client, artist_name, expected_song):
        artist = api_client.get_artist(artist_name)
        top_tracks = api_client.get_artist_top_tracks(artist["id"])
        song_names = [track["name"] for track in top_tracks]
        assert expected_song in song_names, f"Expected {expected_song} in {song_names}"
