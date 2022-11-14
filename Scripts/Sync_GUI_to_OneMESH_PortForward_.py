
import random
import subprocess
import time

from base.WEBLib import Web_Lib
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.AdvancePage import AdvPortForwardPage
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

def add_portforward():
    dataLst = [
                ['1.1.1.1', 'tcp',      'wan', '100', 'lan',  '1100', '123.11.53.25'],
                ['2.2.2.2', 'udp',      'wan', '102', 'lan',  '1200', '123.12.53.25'],
                ['3.3.3.3', 'udp tcp',  'wan', '103', 'lan',  '1300', '123.12.13.25'],
                ['4.4.4.4', 'tcp',      'wan', '104', 'lan',  '1400', '123.14.53.25'],
                ['5.5.5.5', 'udp',      'wan', '150', 'lan',  '1500', '123.15.25.25'],
                ['6.6.6.6', 'udp tcp',  'wan', '160', 'lan',  '1600', '123.12.56.25'],
                ['7.7.7.7', 'tcp',      'wan', '150', 'lan',  '1700', '123.17.53.25'],
                ['8.8.8.8', 'udp',      'wan', '150', 'lan',  '1800', '123.17.53.25']
               ]
    ## Login
    driver = get_driver()
    lp = LoginPage(driver)
    lp.open_url(url_value=url_gui)
    lp.log_in_default()

    advp = AdvPortForwardPage(driver)
    for data in dataLst:
        advp.navigation_to_port_forward()
        advp.setting_port_forward(serviceName=data[0], protocol=data[1], exZone=data[2],
                                        exPort=data[3], inZone=data[4], inPort=data[5],
                                        inIP=data[6], clickApply=True)
        time.sleep(45)
    driver.close()

def edit_portforward():
    dataLst = [
        ['1.1.1.1', 'udp',      'wan', '200', 'lan', '5100', '123.11.53.25'],
        ['2.2.2.2', 'udp tcp',  'wan', '302', 'lan', '5200', '123.12.53.25'],
        ['3.3.3.3', 'tcp',      'wan', '403', 'lan', '500', '123.12.13.25'],
        ['4.4.4.4', 'tcp',      'wan', '504', 'lan', '5400', '123.14.53.25'],
        ['5.5.5.5', 'udp tcp',  'wan', '650', 'lan', '5500', '123.15.25.25'],
        ['6.6.6.6', 'udp',      'wan', '760', 'lan', '5600', '123.12.56.25'],
        ['7.7.7.7', 'udp',      'wan', '850', 'lan', '5700', '123.17.53.25'],
        ['8.8.8.8', 'tcp',      'wan', '950', 'lan', '5800', '123.17.53.25']
    ]
    ## Login
    driver = get_driver()
    lp = LoginPage(driver)
    lp.open_url(url_value=url_gui)
    lp.log_in_default()

    advp = AdvPortForwardPage(driver)
    advp.navigation_to_port_forward()
    for idx, data in enumerate(dataLst):
        advp.edit_port_forward(ruleID=idx, protocol=data[1], exZone=data[2],
                               exPort=data[3], inZone=data[4], inPort=data[5],
                               inIP=data[6], clickApply=True)
        time.sleep(60)
    driver.close()

def delete_all_portforward_from_topdown():
    data = [7, 6, 5, 4, 3, 2, 1]
    ## Login
    driver = get_driver()
    lp = LoginPage(driver)
    lp.open_url(url_value=url_gui)
    lp.log_in_default()

    advp = AdvPortForwardPage(driver)
    advp.navigation_to_port_forward()
    for idx in data:
        advp.delete_port_forward(portID=1)
        time.sleep(45)
    driver.close()

def delete_all_portforward_from_bottomup():
    data = [7, 6, 5, 4, 3, 2, 1, 0]
    ## Login
    driver = get_driver()
    lp = LoginPage(driver)
    lp.open_url(url_value=url_gui)
    lp.log_in_default()

    advp = AdvPortForwardPage(driver)
    advp.navigation_to_port_forward()
    for idx in data:
        advp.delete_port_forward(portID=idx)
        time.sleep(45)
    driver.close()

delete_all_portforward_from_bottomup()