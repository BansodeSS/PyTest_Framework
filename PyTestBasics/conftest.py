import pytest
# parameterisation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=['chrome','firefox'],scope='class')
def init_driver(request):
    if request.param =='chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())

    if request.param =='firefox':
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = web_driver
    yield
    web_driver.close()
