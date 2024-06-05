import allure
import pytest
from allure_commons.types import AttachmentType
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
    @allure.feature('Search Artist')
    @allure.story('Enter the name of the singer to search and check if the singer has a certain song')
    def test_search_artist(self, artist, song, browser):
        with allure.step("Clicking search Button"):
            self.__spotify_home_form.click_search()
        with allure.step(f"Entering artist name: {artist}"):
            self.__spotify_home_form.search_singer(artist)
        with allure.step(f"Asserting if {artist} has the popular song as '{song}'"):
            assert self.__artist_form.is_song_name_exists(song), f"{song} by {artist} not found!"
        png_bytes = browser.driver.get_screenshot_as_png()
        allure.attach(png_bytes, name="Searching artist with popular song", attachment_type=AttachmentType.PNG)

    @pytest.mark.parametrize("artist", [
        "Drake",
        "The Beatles"
    ])
    @pytest.mark.skip(reason="no way of currently testing this")
    @allure.feature('Check if there is a singer in the recent search tab')
    def test_recent_search(self, artist):
        self.__spotify_home_form.click_search()
        assert self.__search_form.check_recent_search(artist), f"{artist} not in recent searches!"
