"""this is class is parent of all test classes """

from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from config import page_load_sleep


class BaseTest:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def sleep_timeout(self):
        sleep(page_load_sleep)

    def do_click(self, element):
        element.click()

    def get_text(self, element):
        return element.text
