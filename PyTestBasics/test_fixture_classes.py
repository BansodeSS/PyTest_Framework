# run the parallel test cases
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# decorators
@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver
    yield
    ch_driver.close()

@pytest.fixture(scope='class')
def init_firefox_driver(request):
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver
    yield
    ff_driver.close()

@pytest.mark.usefixtures('init_chrome_driver')
class Base_Chrome_Test:
    pass
class Test_google_Chrome(Base_Chrome_Test):
    def test_google_title_chrome(self):
        self.driver.get('http://www.google.com')
        assert  self.driver.title =='google'

@pytest.mark.usefixtures('init_firefox_driver')
class Base_Firefox_Test:
    pass
class Test_google_Firefox(Base_Firefox_Test):
    def test_google_title_firefox(self):
        self.driver.get('http://www.google.com')
        assert  self.driver.title =='google'