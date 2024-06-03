from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from framework.locator_constants import LocatorConstant, ElementNameConstant

class ArtistForm(BaseForm):
    __page_name = "Top result"

    def __init__(self):
        super(ArtistForm, self).__init__(
            (By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format(self.__page_name)), self.__page_name)


    def is_song_name_exists(self,song_name):
        song_name = PyQualityServices.element_factory.get_label(
            (By.XPATH, LocatorConstant.PARTIAL_TEXT_LOCATOR.format(song_name)), "Song")
        return song_name.state.is_displayed
