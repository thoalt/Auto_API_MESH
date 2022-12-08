import time

from selenium.webdriver.common.by import By

from base.WEBLib import Web_Lib

class SettingWANPage(Web_Lib):
    def __init__(self, driver):
        super().__init__(driver)

    # Get all locator from main page, sub page
    lnkSettingCap_xpath = "//a[@id='titleSettingCap']"
    lnkWAN_xpath = "//a[@id='sub51']"
    lbWanService_xpath = "//label[@id='LB_WAN_SERIVCE']"

    btnEdit_xpath = "//img[@onclick='EditWan(0);']"
    btnEditWan1_xpath = "//img[@onclick='EditWan(1);']"
    btnEditWan2_xpath = "//img[@onclick='EditWan(2);']"
    btnEditWan3_xpath = "//img[@onclick='EditWan(3);']"

    lnkWanSetBasic_xpath = "//a[contains(text(),'Basic')]"
    lnkWanSetAdv_xpath = "//a[contains(text(),'Advance')]"

    drpService_xpath = "//select[@id='Input_Service']"
    drpIPVersion_xpath = "//select[@id='Input_IPversion']"

    txtIPV4Addr_xpath = "//input[@id='Input_IPv4_Address']"
    drpIPV4Subnet = "//select[@id='Input_IPv4_Netmask']"
    txtIPV4Gateway_xpath = "//input[@id='Input_IPv4_Gateway']"
    txtPRIDNS_xpath = "//input[@id='Input_DNS']"
    txtSECDNS_xpath = "//input[@id='Input_DNS_SECOND']"
    lbIPV4Addr_xpath = "//td[contains(text(),'IPv4 Address')]"

    txtIPV6Addr_xpath = "//input[@id='Input_IPv6_Address']"
    txtIPV6Gateway_xpath = "//input[@id='Input_IPv6_Gateway']"
    lbIPV6Addr_xpath = "//td[contains(text(),'IPv6 Address')]"

    txtMTU_xpath = "//input[@id='Input_MTU']"
    lbOverWrite_xpath = "//td[contains(text(),'Overwrite MTU')]"

    btnNextBasic_xpath = "//input[@onclick='basic_to_advance()']"
    btnApply_xpath = "//input[@onclick='ApplyEdit()']"

    txtPPPoEUser_xpath = "//input[@id='Input_Username']"
    lbPPPoEUser_xpath = "//td[contains(text(),'Username')]"
    txtPPPoEPass_xpath = "//input[@id='Input_Password']"
    lbPPPoEPass_xpath = "//td[contains(text(),'Password')]"

    btnAddWAN_xpath = "//input[@id='button_add_wan']"
    lbInputServer_xpath = "//td[contains(text(),'Server')]"
    txtInputServer_xpath = "//input[@id='Input_Server']"
    txtInputUser_xpath = "//input[@id='Input_Username']"
    txtInputPass_xpath = "//input[@id='Input_Password']"

    # Status Value
    lbIPv4_xpath = "//td[@id='insertWan0Content']/label[@id='LB_IP']"
    lbService_xpath = "//td[@id='insertWan0Content']/label[@id='LB_WAN_SERIVCE']"
    lbIPV6_xpath = "//td[@id='insertWan0Content']/label[@id='LB_IPV6']"
    lbGateway_xpath = "//td[@id='insertWan0Content']/label[@id='LB_GATEWAY']"


    # All Actions
    def click_setting_cap(self):
        self.wait_and_click_element(self.lnkSettingCap_xpath)

    def click_WAN(self):
        self.wait_and_click_element(self.lnkWAN_xpath)

    def get_wantype_overpage(self):
        return self.wait_and_get_property_element(self.lbWanService_xpath, property_name='innerText')

    def click_Edit(self):
        self.wait_and_click_element(self.btnEdit_xpath)

    def click_Edit1(self):
        self.wait_and_click_element(self.btnEditWan1_xpath)

    def click_Edit2(self):
        self.wait_and_click_element(self.btnEditWan2_xpath)

    def click_Edit3(self):
        self.wait_and_click_element(self.btnEditWan3_xpath)

    def click_Basic_Tab(self):
        self.wait_and_click_element(self.lnkWanSetBasic_xpath)

    def click_Advandce_Tab(self):
        self.wait_and_click_element(self.lnkWanSetAdv_xpath)

    def select_service(self, serviceName):
        self.wait_and_select_item(self.drpService_xpath, serviceName)

    def get_service(self):
        return self.wait_and_get_selected_text(self.drpService_xpath)

    def select_IPVersion(self, IPVersion):
        self.wait_and_select_item(self.drpIPVersion_xpath, IPVersion)

    def get_IPVersion(self):
        return self.wait_and_get_selected_text(self.drpIPVersion_xpath)

    def set_IPV4_Addr(self, ipv4_Addr):
        self.wait_and_set_text_element_with_delete(self.txtIPV4Addr_xpath, ipv4_Addr)

    def get_IPV4_Addr(self):
        return self.wait_and_get_attribute_element(xpath=self.txtIPV4Addr_xpath, attribute_name='value')

    def select_IPV4_Netmask(self, netmask):
        self.wait_and_select_item(self.drpIPV4Subnet, netmask)

    def get_IPV4_Netmask(self):
        return self.wait_and_get_selected_text(self.drpIPV4Subnet)

    def set_IPV4_Gateway(self, ipv4_gateway):
        self.wait_and_set_text_element_with_delete(self.txtIPV4Gateway_xpath, ipv4_gateway)

    def get_IPV4_Gateway(self):
        return self.wait_and_get_attribute_element(xpath=self.txtIPV4Gateway_xpath, attribute_name='value')

    def set_Pri_DNS(self, dns):
        self.wait_and_set_text_element_with_delete(self.txtPRIDNS_xpath, dns)

    def get_Pri_DNS(self):
        return self.wait_and_get_attribute_element(xpath=self.txtPRIDNS_xpath, attribute_name='value')

    def set_Sec_DNS(self, dns):
        self.wait_and_set_text_element_with_delete( self.txtSECDNS_xpath, dns)

    def get_Sec_DNS(self):
        return self.wait_and_get_attribute_element(xpath=self.txtSECDNS_xpath, attribute_name='value')

    def set_IPV6_Addr(self, ipv6_addr):
        self.wait_and_set_text_element_with_delete(self.txtIPV6Addr_xpath, ipv6_addr)

    def get_IPV6_Addr(self):
        return self.wait_and_get_attribute_element(xpath=self.txtIPV6Addr_xpath, attribute_name='value')

    def set_IPV6_Gateway(self, ipv6_gateway):
        self.wait_and_set_text_element_with_delete(self.txtIPV6Gateway_xpath, ipv6_gateway)

    def get_IPV6_Gateway(self):
        return self.wait_and_get_attribute_element(xpath=self.txtIPV6Gateway_xpath, attribute_name='value')


    def set_MTU(self, MTUVal):
        self.wait_and_set_text_element_with_delete(self.txtMTU_xpath, MTUVal)

    def click_btn_Next_In_Baic(self):
        self.wait_and_click_element(self.btnNextBasic_xpath)

    def click_Apply(self):
        self.wait_and_click_element(self.btnApply_xpath)

    def set_PPPoE_IPV4_User(self, userName):
        self.wait_and_set_text_element_with_delete(self.txtPPPoEUser_xpath, userName)

    def get_PPPoE_IPV4_User(self):
        return self.wait_and_get_attribute_element(xpath=self.txtPPPoEUser_xpath, attribute_name='value')

    def set_PPPoE_IPV4_Pass(self, password):
        self.wait_and_set_text_element_with_delete(self.txtPPPoEPass_xpath, password)

    def get_PPPoE_IPV4_Pass(self):
        return self.wait_and_get_attribute_element(xpath=self.txtPPPoEPass_xpath, attribute_name='value')

    def click_Add_WAN(self):
        self.wait_and_click_element(self.btnAddWAN_xpath)

    def set_Input_Server(self, serverAddr):
        self.wait_and_set_text_element_with_delete(self.txtInputServer_xpath, serverAddr)

    def get_Input_Server(self):
        return self.wait_and_get_attribute_element(xpath=self.txtInputServer_xpath, attribute_name='value')

    def set_Input_User(self, userName):
        self.wait_and_set_text_element_with_delete(self.txtInputUser_xpath, userName)

    def get_Input_User(self):
        return self.wait_and_get_attribute_element(xpath=self.txtInputUser_xpath, attribute_name='value')

    def set_Input_Password(self, password):
        self.wait_and_set_text_element_with_delete(self.txtInputPass_xpath, password)

    def get_Input_Password(self):
        return self.wait_and_get_attribute_element(xpath=self.txtInputPass_xpath, attribute_name='value')

    def get_default_route(self):
        return self.wait_and_get_checkbox_selected(xpath="//input[@id='Enable_Default_Route']")
    # def get_wan_service(self):
    #     return self.wait_and_get_text_element(self.lbService_xpath)
    #
    # def get_wan_IPv4(self):
    #     return self.wait_and_get_text_element(self.lbIPv4_xpath)
    #
    # def get_wan_IPv6(self):
    #     return self.wait_and_get_text_element(self.lbIPV6_xpath)
    #
    # def get_wan_gateway(self):
    #     return self.wait_and_get_text_element(self.lbGateway_xpath)

    def get_VLAN_ID(self):
        vlanID = ''
        ckb_vlanID = "//input[contains(@id, 'check_interface_eth0')]"
        eleList = self.driver.find_elements(By.XPATH, ckb_vlanID)
        for ele in eleList:
            if ele.get_attribute("checked"):
                valueStr = ele.get_attribute(name='value')
                vlanID = valueStr.split(".")[1]
                break
        return vlanID


    def navigate_to_WAN_page(self):
        self.click_setting_cap()
        time.sleep(1)
        self.click_WAN()
        time.sleep(1)

    def navigate_to_WAN_setting_page(self):
        self.click_setting_cap()
        time.sleep(1)
        self.click_WAN()
        time.sleep(2)
        self.click_Edit()
        time.sleep(2)
        self.click_Basic_Tab()
        time.sleep(1)

    def navigate_to_WAN_1_setting_page(self):
        self.click_setting_cap()
        time.sleep(1)
        self.click_WAN()
        time.sleep(2)
        self.click_Edit1()
        time.sleep(1)
        self.click_Basic_Tab()
        time.sleep(1)

    def navigate_to_WAN_2_setting_page(self):
        self.click_setting_cap()
        time.sleep(1)
        self.click_WAN()
        time.sleep(2)
        self.click_Edit2()
        time.sleep(2)
        self.click_Basic_Tab()
        time.sleep(1)

    def navigate_to_WAN_3_setting_page(self):
        self.click_setting_cap()
        time.sleep(1)
        self.click_WAN()
        time.sleep(2)
        self.click_Edit3()
        time.sleep(2)
        self.click_Basic_Tab()
        time.sleep(1)


    def setting_WAN_IPV4(self, service=None, IPVer=None, IPV4Addr=None, IPV4Net=None,
                         IPV4GW=None, PriDNS=None, SecDNS=None,
                         mtu=None, clickApply=True):
        self.click_Basic_Tab()
        #time.sleep(1)

        if service is not None:
            self.select_service(service)

        if IPVer is not None:
            self.select_IPVersion(IPVer)

        if IPV4Addr is not None:
            self.set_IPV4_Addr(IPV4Addr)

        if IPV4Net is not None:
            self.select_IPV4_Netmask(IPV4Net)

        if IPV4GW is not None:
            self.set_IPV4_Gateway(IPV4GW)

        if PriDNS is not None:
            self.set_Pri_DNS(PriDNS)

        if SecDNS is not None:
            self.set_Sec_DNS(SecDNS)

        if (mtu is not None) or clickApply:
            self.click_btn_Next_In_Baic()

        if mtu is not None:
            self.set_MTU(mtu)

        if clickApply:
            self.click_Apply()

    def setting_WAN_IPV6(self, service=None, IPVer=None, IPV6Addr=None, IPV6GW=None,
                         mtu=None, clickApply=True):
        self.click_Basic_Tab()
        # #time.sleep(1)

        if service is not None:
            self.select_service(service)

        if IPVer is not None:
            self.select_IPVersion(IPVer)

        if IPV6Addr is not None:
            self.set_IPV6_Addr(IPV6Addr)

        if IPV6GW is not None:
            self.set_IPV6_Gateway(IPV6GW)


        if (mtu is not None) or clickApply:
            self.click_btn_Next_In_Baic()

        if mtu is not None:
            self.set_MTU(mtu)

        if clickApply:
            self.click_Apply()


    def setting_WAN_Dual(self, service=None, IPVer=None, IPV4Addr=None, IPV4Net=None,
                         IPV4GW=None, PriDNS=None, SecDNS = None,
                         IPV6Addr=None, IPV6GW=None,
                         mtu = None, clickApply=True):
        self.click_Basic_Tab()
        # #time.sleep(1)

        if service is not None:
            self.select_service(service)

        if IPVer is not None:
            self.select_IPVersion(IPVer)

        if IPV4Addr is not None:
            self.set_IPV4_Addr(IPV4Addr)

        if IPV4Net is not None:
            self.select_IPV4_Netmask(IPV4Net)

        if IPV4GW is not None:
            self.set_IPV4_Gateway(IPV4GW)

        if PriDNS is not None:
            self.set_Pri_DNS(PriDNS)

        if SecDNS is not None:
            self.set_Sec_DNS(SecDNS)

        if IPV6Addr is not None:
            self.set_IPV6_Addr(IPV6Addr)

        if IPV6GW is not None:
            self.set_IPV6_Gateway(IPV6GW)


        if (mtu is not None) or clickApply:
            self.click_btn_Next_In_Baic()

        if mtu is not None:
            self.set_MTU(mtu)

        if clickApply:
            self.click_Apply()

    def setting_WAN_PPPoE(self, IPVer=None, userName=None, pword=None, mtu=None, clickApply=True):
        self.click_Basic_Tab()
        #time.sleep(1)

        if IPVer is not None:
            self.select_IPVersion(IPVer)

        if userName is not None:
            self.set_PPPoE_IPV4_User(userName)

        if pword is not None:
            self.set_PPPoE_IPV4_Pass(pword)

        if mtu is not None:
            self.click_btn_Next_In_Baic()
            self.set_MTU(mtu)

        if clickApply:
            self.click_Apply()

    def settingWAN_L2TP(self, server=None, userName=None, pword=None, mtu=None, clickApply=True):
        self.click_Basic_Tab()
        # #time.sleep(1)

        if server is not None:
            self.set_Input_Server(server)

        if userName is not None:
            self.set_Input_User(userName)

        if pword is not None:
            self.set_Input_Password(pword)

        if mtu is not None:
            self.click_btn_Next_In_Baic()
            self.set_MTU(mtu)

        if clickApply:
            self.click_Apply()

    def settingWAN_PPTP(self, server=None, userName=None, pword=None, mtu=None, clickApply=True):
        self.click_Basic_Tab()
        # #time.sleep(1)

        if server is not None:
            self.set_Input_Server(server)

        if userName is not None:
            self.set_Input_User(userName)

        if pword is not None:
            self.set_Input_Password(pword)

        if mtu is not None:
            self.click_btn_Next_In_Baic()
            self.set_MTU(mtu)

        if clickApply:
            self.click_Apply()

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)