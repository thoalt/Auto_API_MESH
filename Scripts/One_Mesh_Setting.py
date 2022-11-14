import random
import subprocess
import time

from base.WEBLib import Web_Lib
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

def setup():
    try:
        # Kill all process of chromedriver before create new
        subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
    except:
        pass
    url_one_mesh = "http://10.15.151.2:9000/login"
    user_GUI = "one"
    pass_GUI = "one@2019"
    serialNumber = "1292922130B4454"
    serverName = ["1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4",
                  "5.5.5.5", "6.6.6.6", "7.7.7.7", "8.8.8.8"]
    protocol = ["TCP", "UDP", "UDP+TCP"]
    internalIP = ["1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4",
                  "5.5.5.5", "6.6.6.6", "7.7.7.7", "8.8.8.8"]
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
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

    # click tab Port Forwarding
    cltOne.wait_and_click_element(xpath="//a[contains(text(),'PORT FORWARDING')]")
    for idx in range(8, 0):
        btnDel_xpath = f"//h6[contains(text(),'Port Forwarding {str(idx)}')]/following-sibling::div[@class='heading-elements']//i[@class='icon-trash']"
        print("Delete: " + str(idx))
        cltOne.wait_and_click_element(xpath=btnDel_xpath)
        time.sleep(1)
    # for idx in range(0, 8):
    #     #Click button Add
    #     btnAdd_xpath = "//span[@ng-click='addNewPortForwarding()']"
    #     #cltOne.scroll_to_element(xpath=btnAdd_xpath)
    #     cltOne.scroll_to_top_page()
    #     cltOne.wait_and_click_element(xpath=btnAdd_xpath)
    #
    # for idx in range(0, 8):
    #     serName_xpath = f"//h6[contains(text(),'Port Forwarding {str(idx)}')]/parent::div/following-sibling::div[@class='table-responsive']//input[@name='serviceName']"
    #     protocol_xpath = f"//h6[contains(text(),'Port Forwarding {str(idx)}')]/parent::div/following-sibling::div[@class='table-responsive']//select[@name='protocol']"
    #     externalZone_xpath = f"//h6[contains(text(),'Port Forwarding {str(idx)}')]/parent::div/following-sibling::div[@class='table-responsive']//select[@name='externalZone']"
    #     externalPort_xpath = f"//h6[contains(text(),'Port Forwarding {str(idx)}')]/parent::div/following-sibling::div[@class='table-responsive']//input[@name='externalPort']"
    #     internalZone_xpath = f"//h6[contains(text(),'Port Forwarding {str(idx)}')]/parent::div/following-sibling::div[@class='table-responsive']//select[@name='internalZone']"
    #     internalPort_xpath = f"//h6[contains(text(),'Port Forwarding {str(idx)}')]/parent::div/following-sibling::div[@class='table-responsive']//input[@name='internalPort']"
    #     internalIpAddr_xpath = f"//h6[contains(text(),'Port Forwarding {str(idx)}')]/parent::div/following-sibling::div[@class='table-responsive']//input[@name='internalIpAddr']"
    #
    #     cltOne.scroll_to_element(xpath=serName_xpath)
    #     cltOne.wait_and_set_text_with_clear(xpath=serName_xpath, text_value=serverName[idx])
    #
    #     if idx % 3 == 0:
    #         cltOne.wait_and_select_item_by_value(xpath=protocol_xpath, value=protocol[0])
    #     elif idx % 3 == 1:
    #         cltOne.wait_and_select_item_by_value(xpath=protocol_xpath, value=protocol[1])
    #     else:
    #         cltOne.wait_and_select_item_by_value(xpath=protocol_xpath, value=protocol[2])
    #
    #     cltOne.wait_and_select_item_by_value(xpath=externalZone_xpath, value='wan')
    #     cltOne.wait_and_set_text_with_clear(xpath=externalPort_xpath, text_value=str(random.randint(1, 65355)))
    #     cltOne.wait_and_select_item_by_value(xpath=internalZone_xpath, value='lan')
    #     cltOne.wait_and_set_text_with_clear(xpath=internalPort_xpath, text_value=str(random.randint(1, 65355)))
    #     cltOne.wait_and_set_text_with_clear(xpath=internalIpAddr_xpath, text_value=internalIP[idx])
    #
    #     time.sleep(3)

    btnSave_Xpath = "//span[contains(text(),'Port Forwarding Configuration')]/ancestor::div/following-sibling::form[@name='portForwardingForm']//span[text()='Save']"
    cltOne.wait_and_click_element(xpath=btnSave_Xpath)
    time.sleep(30)
    cltOne.quit()

setup()


