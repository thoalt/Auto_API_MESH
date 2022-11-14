import random
import subprocess
import time

from assertpy import assert_that

from base.WEBLib import Web_Lib
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.LoginPage import LoginPage
from pages.SettingWANPage import SettingWANPage
import Utilities.global_dir as gld


def convert_wantype_API_to_GUI(wantypeAPI):
    if wantypeAPI == "dhcp":
        wanType = "DHCP Client"
    elif wantypeAPI == "static":
        wanType = "Static"
    else:
        wanType = "PPPoE"
    return wanType

def conver_IPVer_API_To_GUI(ipVerAPI):
    if ipVerAPI == "dual":
        ipVer = "Dual stack"

    elif ipVerAPI == "ipv4":
        ipVer = "IPv4"

    else:
        ipVer = "IPv6"
    return ipVer


def setup():
    try:
        # Kill all process of chromedriver before create new
        subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
    except:
        pass
    url_one_mesh = "http://10.15.151.2:9000/login"
    url_local_gui = "http://192.168.88.1"

    user_GUI = "one"
    pass_GUI = "one@2019"

    serialNumber = "1292922130B4454"
    driver = webdriver.Chrome(executable_path=gld.DRIVER_FOLDER + "chromedriver.exe")
    driver.implicitly_wait(10)

    cltOne = Web_Lib(driver)
    cltOne.open_url(url_value=url_one_mesh)

    ## Login to Webgui
    cltOne.wait_and_set_text_with_clear(xpath="//input[@name='username']", text_value=user_GUI)
    cltOne.wait_and_set_text_with_clear(xpath="//input[@name='password']", text_value=pass_GUI)
    cltOne.wait_and_click_element(xpath="//button[@id='login-submit']")
    time.sleep(1)

    #Click tab Configuration, search by Serial, then click to detail
    cltOne.wait_and_click_element(xpath="//span[contains(text(),'Configuration')]")
    cltOne.wait_and_set_text_element_with_delete(xpath="//input[@name='serialNumber']", text_value="1292922130B4454")
    serialXpath = f"//a[contains(text(),'{serialNumber}')]"
    # print(serialXpath)
    cltOne.wait_and_click_element(xpath=serialXpath)
    time.sleep(1)

    # click tab WAN
    cltOne.wait_and_click_element(xpath="//a[contains(text(),'WAN')]")

    wanIdx = 0
    wanTypeAfter = "dhcp"
    ipVerAfter = "Dual"

    conType_xpath = f"//h6[contains(text(), 'WAN {str(wanIdx)}')]/parent::div/following-sibling::div[@class='panel-body']//select[@name='connection_type']"
    wanService_xpath = f"//h6[contains(text(), 'WAN {str(wanIdx)}')]/parent::div/following-sibling::div[@class='panel-body']//select[@name='service']"
    user_xpath = f"//h6[contains(text(), 'WAN {str(wanIdx)}')]/parent::div/following-sibling::div[@class='panel-body']//select[@name='username']"
    pass_xpath = f"//h6[contains(text(), 'WAN {str(wanIdx)}')]/parent::div/following-sibling::div[@class='panel-body']//select[@name='password']"
    defaultRoute_xpath = f"//h6[contains(text(), 'WAN {str(wanIdx)}')]/parent::div/following-sibling::div[@class='panel-body']//select[@ng-model='wan.defaultRoute']"
    ipAddress_xpath = f"//h6[contains(text(), 'WAN {str(wanIdx)}')]/parent::div/following-sibling::div[@class='panel-body']//select[@name='ipAddress']"
    subnetMask_xpath = f"//h6[contains(text(), 'WAN {str(wanIdx)}')]/parent::div/following-sibling::div[@class='panel-body']//select[@name='subnetMask']"
    gateway_xpath = f"//h6[contains(text(), 'WAN {str(wanIdx)}')]/parent::div/following-sibling::div[@class='panel-body']//select[@namel='gateway']"
    preferredDns_xpath = f"//h6[contains(text(), 'WAN {str(wanIdx)}')]/parent::div/following-sibling::div[@class='panel-body']//select[@name='preferredDns']"
    alternateDns_xpath = f"//h6[contains(text(), 'WAN {str(wanIdx)}')]/parent::div/following-sibling::div[@class='panel-body']//select[@name='alternateDns']"
    btnSave_Xpath = "//span[contains(text(),'WAN configuration')]/ancestor::div/following-sibling::form[@name='wanForm']//span[text()='Save']"

    cltOne.wait_and_select_item(xpath=conType_xpath, text_item=wanTypeAfter)
    cltOne.wait_and_select_item(xpath=wanService_xpath, text_item=ipVerAfter)

    cltOne.wait_and_click_element(xpath=btnSave_Xpath)
    time.sleep(30)

    cltOne.open_new_windown(url_value=url_local_gui)
    cltOne.open_url(url_local_gui)
    lp = LoginPage(driver)
    lp.log_in_default()

    wp = SettingWANPage(driver)
    wp.navigate_to_WAN_page()

    wanTypeGUI = convert_wantype_API_to_GUI(wanTypeAfter)
    ipVerGui = conver_IPVer_API_To_GUI(ipVerAfter)

    assert_that(wanTypeGUI).is_equal_to(wp.get_service())
    assert_that(ipVerGui).is_equal_to(wp.get_IPVersion())

    cltOne.quit()

setup()


