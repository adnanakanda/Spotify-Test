from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from framework.locator_constants import LocatorConstant, ElementNameConstant

class SpotifyHomeForm(BaseForm):
    __page_name = "Popular artists"
    __search_btn = PyQualityServices.element_factory.get_button(
        (By.XPATH, ("//a[@aria-label='Search']")), "Search button")
    __search_field = PyQualityServices.element_factory.get_text_box((By.XPATH, ("//input[@placeholder='What do you want to play?']")),"Singer name")

    def __init__(self):
        super(SpotifyHomeForm, self).__init__(
            (By.XPATH, LocatorConstant.PRECISE_TEXT_LOCATOR.format(self.__page_name)), self.__page_name)

    def click_search(self):
        self.__search_btn.click()

    def search_singer(self,name):
        self.__search_field.clear_and_type(name)
