# run the parallel test cases
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest
from webdriver_manager.chrome import ChromeDriverManager
driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.google.com/')

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title =="Google"

def test_google_url():
    assert driver.current_url =="https://www.google.com/"