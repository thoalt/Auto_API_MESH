import time

from base.WEBLib import Web_Lib

class SettingLANPage(Web_Lib):
    # Get all locator from Mainpage
    # Get all locator from main page, sub page
    lnkSettingCap_xpath = "//a[@id='titleSettingCap']"
    lnkLAN_xpath = "//a[@id='sub52']"
    imgEdit_xpath = "//img[@onclick='EditLan(0);']"
    lbLanOverview_xpath = "//td[contains(text(),'LAN Overview')]"
    btnEdit_xpath = ""

    txtIPV4Addr_xpath = "//input[@id='Input_IPv4_Address']"
    lbIPVersion_xpath = "//td[contains(text(),'IP Version')]"

    drpIPVersion_xpath = "//select[@id='Input_IPversion']"
    drpNetmask_xpath = "//select[@id='Input_IPv4_Netmask']"

    lbDHCPVer4_xpath = "//td[contains(text(),'Start IP Address')]"
    txtStartIP_xpath = "//input[@id='Input_Start_IP']"
    txtNumIPAddrs_xpath = "//input[@id='Input_Number_IP']"
    txtLeaseTime_xpath = "//input[@id='Input_Lease_Time']"

    lbOverWrite_xpath = "//td[contains(text(),'Overwrite MTU')]"
    txtMTU_xpath = "//input[@id='Input_MTU']"

    lnkLanSetBasic_xpath = "//a[contains(text(),'Basic')]"
    lnkLanSetDHCP_xpath = "//a[contains(text(),'DHCP Server')]"
    lnkLanSetAdv_xpath = "//a[contains(text(),'Advance')]"

    txtAssigLengh_xpath = "//input[@id='Input_Length_V6']"
    drpDHCPMode_xpath = "//select[@id='Input_DHCP_Mode_v6']"
    lbDHCPMode_xpath = "//td[contains(text(),'DHCPv6 Mode')]"

    txtPrefixV6_xpath = "//input[@id='Input_Prefix_V6']"
    txtPriV6DNS_xpath = "//input[@id='Input_Pri_V6']"
    txtSecV6DNS_xpath = "//input[@id='Input_Second_V6']"

    btnNextBasicToDHCP_xpath = "//input[@onclick='basic_to_dhcp()']"
    btnNextDHCPToAdv_xpath = "//input[@onclick='dhcp_to_advance()']"
    btnApply_xpath = "//input[@onclick='ApplyEdit()']"

    popupBlock_xpath = "//div[@id='pop-background' and @style='display: block;']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_setting_cap(self):
        self.wait_and_click_element(self.lnkSettingCap_xpath)

    def click_LAN(self):
        self.wait_and_click_element(self.lnkLAN_xpath)

    def click_edit(self):
        self.wait_and_click_element(self.imgEdit_xpath)

    def click_basic_tab(self):
        self.wait_and_click_element(self.lnkLanSetBasic_xpath)

    def click_DHCP_tab(self):
        self.wait_and_click_element(self.lnkLanSetDHCP_xpath)

    def click_advandce_tab(self):
        self.wait_and_click_element(self.lnkLanSetAdv_xpath)

    def select_IP_Version(self, IPVersion):
        self.wait_and_select_item(self.drpIPVersion_xpath, IPVersion)

    def get_IP_version(self):
        return self.wait_and_get_selected_text(self.drpIPVersion_xpath)

    def set_IPV4_addr(self, ipv4_Addr):
        self.wait_and_set_text_element_with_delete(self.txtIPV4Addr_xpath, ipv4_Addr)

    def get_IPV4_addr(self):
        return self.wait_and_get_attribute_element(self.txtIPV4Addr_xpath, 'value')

    def select_netmask(self, netmask):
        self.wait_and_select_item(self.drpNetmask_xpath, netmask)

    def get_netmask(self):
        return self.wait_and_get_selected_text(self.drpNetmask_xpath)

    def set_start_IPAddr(self, startIP):
        self.wait_and_set_text_element_with_delete(self.txtStartIP_xpath, startIP)

    def get_start_IPAddr(self):
        return self.wait_and_get_attribute_element(self.txtStartIP_xpath, 'value')

    def set_number_IP(self, numberIP):
        self.wait_and_set_text_element_with_delete(self.txtNumIPAddrs_xpath, numberIP)

    def get_number_IP(self):
        return self.wait_and_get_attribute_element(self.txtNumIPAddrs_xpath, 'value')

    def set_lease_time(self, leaseTime):
        self.wait_and_set_text_element_with_delete(self.txtLeaseTime_xpath, leaseTime)

    def get_lease_time(self):
        return self.wait_and_get_attribute_element(self.txtLeaseTime_xpath, 'value')

    def set_MTU(self, MTUVal):
        self.wait_and_set_text_element_with_delete(self.txtMTU_xpath, MTUVal)

    def get_MTU(self):
        return self.wait_and_get_attribute_element(self.txtMTU_xpath, 'value')

    def click_btn_next_in_baic(self):
        self.wait_and_click_element(self.btnNextBasicToDHCP_xpath)

    def click_btn_next_in_DHCP(self):
        self.wait_and_click_element(self.btnNextDHCPToAdv_xpath)

    def click_apply(self):
        self.wait_and_click_element(self.btnApply_xpath)

    def set_ipV6_assignent_length(self, length):
        self.wait_and_set_text_element_with_delete(self.txtAssigLengh_xpath, length)

    def select_DHCP_Mode(self, dhcpMode):
        self.wait_and_select_item(self.drpDHCPMode_xpath, dhcpMode)

    def set_Prefix_V6(self, prefix):
        self.wait_and_set_text_element_with_delete(self.txtPrefixV6_xpath, prefix)

    def set_PriDNS_V6(self, dnsVal):
        self.wait_and_set_text_element_with_delete(self.txtPriV6DNS_xpath, dnsVal)

    def set_SecDNS_V6(self, dnsVal):
        self.wait_and_set_text_element_with_delete(self.txtSecV6DNS_xpath, dnsVal)

    def navigate_to_LAN_Setting_tab(self):
        self.click_setting_cap()
        time.sleep(1)
        self.click_LAN()
        time.sleep(1)
        self.click_edit()
        time.sleep(1)

    def navigate_to_DHCP_tab(self):
        self.click_setting_cap()
        time.sleep(1)
        self.click_LAN()
        time.sleep(1)
        self.click_edit()
        time.sleep(1)
        self.click_DHCP_tab()
        time.sleep(2)

    def set_LAN_value(self, ipVer=None, ipAddr=None, netMask=None,
                     startIP=None, numIP=None, leaseTime=None,
                     overMTU=None, clickApply=True):

        self.click_basic_tab()
        if ipVer is not None:
            self.select_IP_Version(ipVer)

        if ipAddr is not None:
            self.set_IPV4_addr(ipAddr)

        if netMask is not None:
            self.select_netmask(netMask)

        if (startIP is not None) or\
            (numIP is not None) or \
            (leaseTime is not None) or \
            (overMTU is not None) or \
            clickApply:
            self.click_btn_next_in_baic()

        if startIP is not None:
            self.set_start_IPAddr(startIP)

        if numIP is not None:
            self.set_number_IP(numIP)

        if leaseTime is not None:
            self.set_lease_time(leaseTime)

        if overMTU is not None or clickApply:
            self.click_btn_next_in_DHCP()

        if overMTU is not None:
            self.set_MTU(overMTU)

        if clickApply:
            self.click_apply()


    def set_LAN_IPV6_value(self, ipVer=None,
                     assignLength=None, dhcpV6Mode=None,
                     priDns=None, secDNS=None,
                     overMTU=None, clickApply=True):

        self.click_basic_tab()
        if ipVer is not None:
            self.select_IP_Version(ipVer)

        if (assignLength is not None) or \
            (dhcpV6Mode is not None) or \
            (priDns is not None) or \
            (secDNS is not None) or \
            (overMTU is not None):
            self.click_btn_next_in_baic()

        if assignLength is not None:
            self.set_ipV6_assignent_length(assignLength)

        if dhcpV6Mode is not None:
            self.select_DHCP_Mode(dhcpV6Mode)

        if priDns is not None:
            self.set_PriDNS_V6(priDns)

        if secDNS is not None:
            self.set_SecDNS_V6(secDNS)

        if overMTU is not None:
            self.click_btn_next_in_DHCP()
            self.set_MTU(overMTU)

        if clickApply:
            self.click_apply()


    def set_LAN_Dual_value(self, ipVer=None,
                     startIP=None, numIP=None, leaseTime=None,
                     assignLength=None, dhcpV6Mode=None,
                     priDns=None, secDNS=None,
                     overMTU=None, clickApply=True):

        self.click_basic_tab()
        if ipVer is not None:
            self.select_IP_Version(ipVer)

        if (startIP is not None) or\
            (numIP is not None) or \
            (leaseTime is not None) or \
            (assignLength is not None) or \
            (dhcpV6Mode is not None) or \
            (priDns is not None) or \
            (secDNS is not None) or \
            (overMTU is not None):
            self.click_btn_next_in_baic()

        if startIP is not None:
            self.set_start_IPAddr(startIP)

        if numIP is not None:
            self.set_number_IP(numIP)

        if leaseTime is not None:
            self.set_lease_time(leaseTime)

        if assignLength is not None:
            self.set_ipV6_assignent_length(assignLength)

        if dhcpV6Mode is not None:
            self.select_DHCP_Mode(dhcpV6Mode)

        if priDns is not None:
            self.set_PriDNS_V6(priDns)

        if secDNS is not None:
            self.set_SecDNS_V6(secDNS)

        if overMTU is not None:
            self.click_btn_next_in_DHCP()
            self.set_MTU(overMTU)

        if clickApply:
            self.click_apply()

    def get_LAN_setting(self):
        self.click_basic_tab()
        interface = 'lan'
        ipVersion = self.get_IP_version()
        ipV4Addr = self.get_IPV4_addr()
        subnet = self.get_netmask()

        self.click_btn_next_in_baic()
        dhcpServer = 'Enable'
        startIP = self.get_start_IPAddr()
        numberIP = self.get_number_IP()
        leaseTime = self.get_lease_time()

        self.click_btn_next_in_DHCP()
        mtu = self.get_MTU()

        return [interface, ipVersion, ipV4Addr, subnet,
                dhcpServer, startIP, numberIP, leaseTime,
                mtu]

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)