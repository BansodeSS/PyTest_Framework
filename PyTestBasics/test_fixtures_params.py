# run the parallel test cases
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# decorators
@pytest.fixture(params=['chrome','firefox'],scope='class')
def init_driver(request):
    if request.param =='chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())

    if request.param =='firefox':
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures('init_driver')
class Base_Test:
    pass
# fixtures examples
class Test_google(Base_Test):
    def test_google_title(self):
        self.driver.get('http://www.google.com')
        assert  self.driver.title =='Google'