import pytest
from framework.forms.artist_form import ArtistForm
from framework.forms.search_form import SearchForm
from framework.forms.spotify_home_form import SpotifyHomeForm

@pytest.mark.xdist_group(name="UI")
class TestSpotifyUI:
    __spotify_home_form: SpotifyHomeForm = SpotifyHomeForm()
    __artist_form: ArtistForm = ArtistForm()
    __search_form: SearchForm = SearchForm()

    @pytest.mark.parametrize("artist, song", [
        ("Drake", "One Dance"),
        ("The Beatles", "Here Comes The Sun - Remastered 2009")
    ])

    def test_search_artist(self, artist,song):

        self.__spotify_home_form.click_search()
        self.__spotify_home_form.search_singer(artist)
        assert self.__artist_form.is_song_name_exists(song), f"{song} by {artist} not found!"

    @pytest.mark.parametrize("artist", [
        "Drake",
        "The Beatles"
    ])
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_recent_search(self, artist):
        self.__spotify_home_form.click_search()
        assert self.__search_form.check_recent_search(artist), f"{artist} not in recent searches!"
