# run the parallel test cases
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest
from webdriver_manager.chrome import ChromeDriverManager
driver = None
# decorators

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print('--------set Up--------')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.google.com/')
    yield
    print('---------tear Down----------')
    driver.quit()

def test_google_title(init_driver):
    assert driver.title =="Google"

def test_google_url(init_driver):
    assert driver.current_url =="https://www.google.com/"