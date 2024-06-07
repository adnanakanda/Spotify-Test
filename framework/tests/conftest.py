import allure
import pytest
from browser.py_quality_services import PyQualityServices
from core.utilities.json_settings_file import JsonSettingsFile
from framework.utils.browser_factory import BrowserFactory
from framework.utils.spotify_client import SpotifyClient


def pytest_sessionstart(session):
    PyQualityServices.browser_factory = BrowserFactory()
    PyQualityServices.get_browser()

@pytest.fixture(scope="session", autouse = True)
def browser(request):
    settings = JsonSettingsFile("config.json")

    browser = PyQualityServices.get_browser()
    browser.maximize()
    browser.go_to(settings.get_value("url"))

    yield browser

    browser.quit()

@pytest.fixture(scope="session")
def api_client():
    return SpotifyClient()

@pytest.fixture(scope='function', autouse=True)
def screenshot_on_failure(request,browser):
    yield
    # If the test failed, take a screenshot
    if request.node.rep_call.failed:
        screenshot = browser.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
