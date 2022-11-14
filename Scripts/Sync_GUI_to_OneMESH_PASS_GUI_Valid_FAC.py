
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
                'ttcn@99C',
                'ttcn @99C',
                'ttcn@99CN1aB%^. ttcn@99CN1aB%^.!',
                'ttcn7@CNab',
                'ttcn@Ovn12',
                'TtCN1@3CN',
                'ttcn11CN/m',
                'ttcn11CN*m',
                'ttcn11CN@m',
                'ttcn11CN#m',
                'ttcn11CN.m',
                'ttcn11CN$m',
                'ttcn11CN~m',
                'ttcn11CN`m',
                'ttcn11CN!m',
                'ttcn11CN%m',
                'ttcn11CN!m',
                'ttcn11CN%m',
                'ttcn11CN^m',
                'ttcn11CN(m',
                'ttcn11CN)m',
                'ttcn11CN-m',
                'ttcn11CN+m',
                'ttcn11CN_m',
                'ttcn11CN=m',
               ]
    # Reset Factory befor setting
    serialClt = Serial_Lib()
    serialClt.Reset_Factory()

    driver = get_driver()
    lp = LoginPage(driver)
    lp.open_url(url_value=url_gui)
    lp.log_in_default()

    for idx, data in enumerate(dataLst):
        ## Login
        print(data)
        if idx == 0:
            sp = SystemManagerPage(driver)
            sp.navigate_to_administrator_page()

            sp.change_admin_pass(oldPass='VNPT',
                                 newPass=data,
                                 confirmPass=data,
                                 clickBtnUpdate=True)
            time.sleep(5)

        else:
            lp.log_in_to_webgui(username='root', password=dataLst[idx-1])

            sp = SystemManagerPage(driver)
            sp.navigate_to_administrator_page()

            sp.change_admin_pass(oldPass=dataLst[idx-1],
                                 newPass=data,
                                 confirmPass=data,
                                 clickBtnUpdate=True)
            time.sleep(5)

    driver.close()

setting_pass_GUI()
