import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from config import gecko_driver, headless, page_load_sleep, site_base_url, user_agent

try:
    current_path = os.path.dirname(os.path.abspath(__file__))
except Exception:
    current_path = "."


def init_driver(_gecko_driver=gecko_driver, _user_agent=user_agent, load_images=True, is_headless=False):
    firefox_profile = webdriver.FirefoxProfile()

    firefox_profile.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", False)
    firefox_profile.set_preference("media.volume_scale", "0.0")
    firefox_profile.set_preference("dom.webnotifications.enabled", False)
    if user_agent != "":
        firefox_profile.set_preference("general.useragent.override", _user_agent)
    if not load_images:
        firefox_profile.set_preference("permissions.default.image", 2)

    options = Options()
    options.headless = is_headless

    driver = webdriver.Firefox(options=options, executable_path=f"{current_path}/{_gecko_driver}", firefox_profile=firefox_profile)

    return driver
