from time import sleep

import pytest

from general import init_driver, site_base_url


@pytest.fixture(autouse=True)
def driver():

    driver = init_driver()
    # # 1
    driver.get(site_base_url)
    yield driver
    driver.quit()


# driver = init_driver()
# 1
# driver.get(site_base_url)
# 1
def test_connection():
    pass


# 2.a
def test_logo(driver):

    logo = driver.find_elements_by_css_selector(".navbar-header a.navbar-brand img")
    assert logo[0] is not None


# 2.c
def test_drop_down_codes(driver):

    codes_drop_down_menu = driver.find_elements_by_xpath("/html/body/div[2]/div/div[3]/ul/li[1]/a")

    assert len(codes_drop_down_menu) > 0

    assert codes_drop_down_menu[0].text == "Codes"
    aria_expanded = codes_drop_down_menu[0].get_attribute("aria-expanded")
    assert not bool(aria_expanded)
    codes_drop_down_menu[0].click()
    sleep(2)
    aria_expanded = codes_drop_down_menu[0].get_attribute("aria-expanded")
    assert bool(aria_expanded)


# 2.d,e,f
def test_search_output(driver):

    search_bar = driver.find_elements_by_css_selector(".form-group")[0]
    # 2.d:check if search_bar upper 200 pixel at screen
    assert search_bar.get("y") < 200
    search_inputs = driver.find_elements_by_xpath("""//*[@id="searchText"]""")
    search_btns = driver.find_elements_by_id("search")
    assert len(search_inputs) > 0 and len(search_btns) > 0
    search_input = search_inputs[0]
    search_btn = search_btns[0]
    # 2.e write this code to search bar and click
    search_input.send_keys("U07.1")
    search_btn.click()

    # 2.f get the result of search
    list_a = driver.find_elements_by_css_selector(".body-content .searchLine  strong a")
    assert len(list_a) > 0
    result_ICD = None
    print(len(list_a), list_a)
    for a in list_a:
        # 2.get the result of search
        print(a.text)
        if a.text.strip() == "ICD-10-CM Diagnosis Code U07.1":

            result_ICD = a.text.strip()
    # 2.f  expected result check if exist
    assert result_ICD is not None
