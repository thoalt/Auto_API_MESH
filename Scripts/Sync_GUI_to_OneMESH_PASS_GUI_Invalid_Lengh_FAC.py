
import random
import subprocess
import time

import assertpy
from assertpy import assert_that, soft_assertions

from base.SerialLib import Serial_Lib
from base.WEBLib import Web_Lib
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.LoginPage import LoginPage
from pages.SystemPage import SystemManagerPage
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

def setting_pass_GUI():
    dataLst = [
                'ttcn@99',
                'ttcn@99CN1aB%^.!ttcn@99CN1aB%^.!2'
               ]
    ## Login
    # Reset Factory befor setting
    serialClt = Serial_Lib()
    serialClt.Reset_Factory()

    expAlert = "Invalid length"
    driver = get_driver()
    lp = LoginPage(driver)
    lp.open_url(url_value=url_gui)
    lp.log_in_default()
    alert_Lst = []

    sp = SystemManagerPage(driver)
    sp.navigate_to_administrator_page()

    for data in dataLst:
        sp.change_admin_pass(newPass=data, clickBtnUpdate=False)
        alert = sp.get_alert_info()
        alert_Lst.append(alert)
        time.sleep(1)
    driver.close()

    for idx, item in enumerate(alert_Lst):
        assert_that(str(item), description=f"<{dataLst[idx]}>").contains(expAlert)
setting_pass_GUI()

