from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from framework.locator_constants import LocatorConstant, ElementNameConstant

class SearchForm(BaseForm):
    __page_name = "Recent searches"

    def __init__(self):
        super(SearchForm, self).__init__(
            (By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format(self.__page_name)), self.__page_name)


    def check_recent_search(self, artist_name):
        name_lbl = PyQualityServices.element_factory.get_label(
            (By.XPATH, LocatorConstant.PARTIAL_TEXT_LOCATOR.format(artist_name)), "Song")
        return name_lbl.state.is_displayed
