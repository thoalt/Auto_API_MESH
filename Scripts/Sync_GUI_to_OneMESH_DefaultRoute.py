
import random
import subprocess
import time

from base.WEBLib import Web_Lib
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.AdvancePage import AdvRouteSetPage
from pages.LoginPage import LoginPage
import Config.config as cfg

url_gui = "http://192.168.88.1/"
def get_driver():
    try:
        # Kill all process of chromedriver before create new
        subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
    except:
        pass
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    return driver

def setting_default_route():
    dataLst = [
                ['lan', '192.167.21.2', '255.255.255.0', '123.11.53.25', '100', '1500'],
                ['wan', '192.167.21.2', '255.255.0.0', '123.12.53.25', '102', '1500'],
                ['lan', '10.167.21.2', '255.0.0.0', '123.12.13.25', '103', '1500'],
                ['wan', '192.167.21.2', '255.255.255.0', '123.14.53.25', '104', '1500'],
                ['lan', '100.167.21.2', '255.255.0.0', '123.15.25', '150', '1500'],
                ['wan', '192.167.21.2', '255.0.0.0', '123.12.56.25', '160', '1500'],
                ['lan', '178.167.21.2', '255.255.255.0', '123.17.53.25', '150', '1500']
               ]
    ## Login
    driver = get_driver()
    lp = LoginPage(driver)
    lp.open_url(url_value=url_gui)
    lp.log_in_default()

    advp = AdvRouteSetPage(driver)
    for data in dataLst:
        advp.navigate_to_add_route_page()
        advp.setting_new_route(interface=data[0], ipAddr=data[1], netmask=data[2],
                                        gateway=data[3], metric=data[4], mtu=data[5],
                                        clickApply=True)
        time.sleep(45)
