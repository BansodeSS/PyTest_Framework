# parameterisation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
@pytest.mark.usefixtures('init_driver')
class BaseClass:
    pass

class TesthubSpot(BaseClass):
    @pytest.mark.parametrize(

        'username,password',[
        ('admin@gmail.com','admin123'),
        ('suhas@gmail.com','suhas123')]
    )
    def test_login(self,username,password):
        ''' This method use to login to hubspot
        :param username:
        :param password:
        :return:
        '''
        self.driver.get('https://app.hubspot.com/login')
        self.driver.find_element(By.ID,'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)

#
