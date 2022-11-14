import time

from base.WEBLib import Web_Lib

class AdvancePage(Web_Lib):
    def __init__(self, driver):
        super().__init__(driver)

    lnkAdvanceTab_xpath = "//a[@id='titleAdances']"
    lnkHomeWifi_xpath = "//a[@id='titehomewifi']"
    lnkInetTime_xpath = "//a[@id='sub47']"
    lnkDiagnostic_xpath = "//a[@id='sub48']"
    lnkDDNS_xpath  = "//a[@id='sub49']"
    lnkPortForward_xpath = "//a[@id='sub50']"
    lnkVLAN_xpath = "//a[@id='sub41']"
    lnkFirewall_xpath = "//a[@id='sub42']"
    lnkRoute_xpath = "//a[@id='sub43']"

    def click_Advanced(self):
        self.wait_and_click_element(self.lnkAdvanceTab_xpath)

    def click_HomeWifi(self):
        self.wait_and_click_element(self.lnkHomeWifi_xpath)

    def click_InetTime(self):
        self.wait_and_click_element(self.lnkInetTime_xpath)

    def click_Diagnostic(self):
        self.wait_and_click_element(self.lnkDiagnostic_xpath)

    def click_DDNS(self):
        self.wait_and_click_element(self.lnkDDNS_xpath)

    def click_PortForward(self):
        self.wait_and_click_element(self.lnkPortForward_xpath)

    def click_VLAN(self):
        self.wait_and_click_element(self.lnkVLAN_xpath)

    def click_Firewall(self):
        self.wait_and_click_element(self.lnkFirewall_xpath)

    def click_Route(self):
        self.wait_and_click_element(self.lnkRoute_xpath)

    def click_delete_ddns0(self):
        self.wait_and_click_element(xpath="//img[@onclick='DeleteRule(0)']")
        time.sleep(1)
        self.accept_alert()
        time.sleep(2)

    def navigation_to_home_wifi(self):
        self.click_Advanced()
        time.sleep(1)
        self.click_HomeWifi()
        time.sleep(1)

    def navigation_to_internettime(self):
        self.click_Advanced()
        time.sleep(1)
        self.click_InetTime()
        time.sleep(1)

    def navigation_to_diagnostic(self):
        self.click_Advanced()
        time.sleep(1)
        self.click_Diagnostic()
        time.sleep(1)

    def navigation_to_ddns(self):
        self.click_Advanced()
        time.sleep(1)
        self.click_DDNS()
        time.sleep(1)

    def navigation_to_port_forward(self):
        self.click_Advanced()
        time.sleep(1)
        self.click_PortForward()
        time.sleep(1)

    def navigation_to_VLAN(self):
        self.click_Advanced()
        time.sleep(1)
        self.click_VLAN()
        time.sleep(1)

    def navigation_to_firewall(self):
        self.click_Advanced()
        time.sleep(1)
        self.click_Firewall()
        time.sleep(1)

    def navigation_to_route(self):
        self.click_Advanced()
        time.sleep(1)
        self.click_Route()
        time.sleep(1)


class AdvHomeWifiPage(AdvancePage):
    def __init__(self, driver):
        super().__init__(driver)

    lnkURLFilter_xpath = "//a[@id='sub44']"
    lnkAccessControl_xpath = "//a[@id='sub45']"
    lnkLedControl_xpath = "//a[@id='sub46']"
    txtInputUrl_xpath = "//input[@id='input_url_input']"
    lbIndexAdd_xpath = "//td[contains(text(),'Index')]"

    btnAddRule_xpath = "//input[@onclick='ApplyNewULR();']"

    txtGroupName_xpath = "//input[@id='groupname']"
    cbkMon_xpath = "//input[@id='checkmon']"
    cbkTue_xpath = "//input[@id='checktue']"
    cbkWed_xpath = "//input[@id='checkwed']"
    cbkThu_xpath = "//input[@id='checkthu']"
    cbkFri_xpath = "//input[@id='checkfri']"
    cbkSat_xpath = "//input[@id='checksat']"
    cbkSun_xpath = "//input[@id='checksat']"
    cbkAll_xpath = "//input[@id='checkall']"
    drpStartHour_xpath = "//select[@id='starttime_hour']"
    drpStartMin_xpath = "//select[@id='starttime_minute']"
    drpEndHour_xpath = "//select[@id='stoptime_hour']"
    drpEndMin_xpath = "//select[@id='stoptime_minute']"

    lnkClientMac_xpath = "//span[@onclick='LinktoClient(0)']"
    txtMacAddr_xpath = "//input[@id='add_input']"
    btnAddNewMac_xpath = "//input[@onclick='AddNewMac(0)']"

    lnkURL_xpath = "//span[@onclick='LinktoURL(0)']"
    txtUrlLink_xpath = "//input[@id='input_url_input']"
    btnAddNewUrl_xpath = "//input[@onclick='AddNewURL(0)']"

    btnAddGroup_xpath = "//input[@onclick='ApplyNew();']"
    btnDeletGroup_xpath = "//img[@onclick='DeleteGroup(%s)']"

    def click_URL_Filter(self):
        self.wait_and_click_element(self.lnkURLFilter_xpath)

    def click_Access_Control(self):
        self.wait_and_click_element(self.lnkAccessControl_xpath)

    def set_Input_URL(self, urlVal):
        self.wait_and_set_text_element_with_delete(self.txtInputUrl_xpath, urlVal)

    def click_Btn_AddRule(self):
        self.wait_and_click_element(self.btnAddRule_xpath)

    def set_GroupName(self, groupName):
        self.wait_and_set_text_element_with_delete(self.txtGroupName_xpath, groupName)

    def checkAll(self):
        self.wait_and_check_checkbox(self.cbkAll_xpath)

    def select_Time_Start(self, sHour, sMin):
        self.wait_and_select_item(self.drpStartHour_xpath, sHour)
        self.wait_and_select_item(self.drpStartMin_xpath, sMin)

    def select_Time_End(self, eHour, eMin):
        self.wait_and_select_item(self.drpEndHour_xpath, eHour)
        self.wait_and_select_item(self.drpEndMin_xpath, eMin)

    def click_Btn_Add_Group(self):
        self.wait_and_click_element(self.btnAddGroup_xpath)

    def click_Btn_Delete_Group(self, groupID):
        self.wait_and_click_element(self.btnDeletGroup_xpath %groupID)

    def click_client_link(self):
        self.wait_and_click_element(self.lnkClientMac_xpath)

    def set_client_mac(self, macAddr):
        self.wait_and_set_text_element_with_delete(self.txtMacAddr_xpath, macAddr)

    def click_btn_add_new_mac(self):
        self.wait_and_click_element(self.btnAddNewMac_xpath)

    def click_url_link(self):
        self.wait_and_click_element(self.lnkURL_xpath)

    def set_url_link(self, url):
        self.wait_and_set_text_element_with_delete(self.txtUrlLink_xpath, url)

    def click_btn_add_new_url(self):
        self.wait_and_click_element(self.btnAddNewUrl_xpath)

    def navigate_to_URL_Filter_Page(self):
        self.navigation_to_home_wifi()
        time.sleep(1)
        self.click_URL_Filter()
        time.sleep(1)

    def navigate_to_Access_Control_page(self):
        self.navigation_to_home_wifi()
        time.sleep(1)
        self.click_Access_Control()
        time.sleep(1)

    def setting_url_filter(self, url=None, clickApply=False):
        if url is not None:
            self.set_Input_URL(url)

        if clickApply:
            self.click_Btn_AddRule()

    def setting_group_access_control(self, groupName=None, clickApply=False):
        if groupName is not None:
            self.set_GroupName(groupName)

        if clickApply:
            self.click_Btn_Add_Group()

    def setting_access_control_mac(self, clientMac= None, clickApply=False):
        if clientMac is not None:
            self.set_client_mac(clientMac)

        if clickApply:
            self.click_btn_add_new_mac()

    def setting_access_control_url(self, url=None, clickApply=False):
        #self.click_url_link()
        if url is not None:
            self.set_url_link(url)

        if clickApply:
            self.click_btn_add_new_url()


    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)


class AdvInternetTimePage(AdvancePage):
    def __init__(self, driver):
        super().__init__(driver)

    cbkNTPenable_xpath = "//input[@id='ntpEnabled']"
    txtHostName_xpath = "//input[@id='Hostname']"
    txtPriServer_xpath = "//input[@id='ntpServerOther1']"
    drpPriServer_xpath = "//select[@id='ntpServer1']"
    txtSecServer_xpath = "//input[@id='ntpServerOther2']"
    drpSecServer_xpath = "//select[@id='ntpServer2']"
    txtThirServer_xpath = "//input[@id='ntpServerOther3']"
    drpThirServer_xpath = "//select[@id='ntpServer3']"
    txtFourServer_xpath = "//input[@id='ntpServerOther4']"
    drpFourServer_xpath = "//select[@id='ntpServer4']"
    btnApply_xpath = "//input[@onclick='btnApply()']"

    def get_ntp_status(self):
        return self.wait_and_get_checkbox_selected(self.cbkNTPenable_xpath)

    def set_hostname(self, hostname):
        self.wait_and_set_text_element_with_delete(self.txtHostName_xpath, hostname)

    def get_hostname(self):
        return self.wait_and_get_attribute_element(self.txtHostName_xpath, 'value')

    def select_pri_server(self, server):
        self.wait_and_select_item(self.drpPriServer_xpath, server)

    def set_pri_server(self, server):
        self.wait_and_set_text_element_with_delete(self.txtPriServer_xpath, server)

    def get_pri_serer(self):
        return self.wait_and_get_selected_text(self.drpPriServer_xpath)

    def select_sec_server(self, server):
        self.wait_and_select_item(self.drpSecServer_xpath, server)

    def set_sec_server(self, server):
        self.wait_and_set_text_element_with_delete(self.txtSecServer_xpath, server)

    def get_sec_serer(self):
        return self.wait_and_get_selected_text(self.drpSecServer_xpath)

    def select_thir_server(self, server):
        self.wait_and_select_item(self.drpThirServer_xpath, server)

    def set_thir_server(self, server):
        self.wait_and_set_text_element_with_delete(self.txtThirServer_xpath, server)

    def get_thir_serer(self):
        return self.wait_and_get_selected_text(self.drpThirServer_xpath)

    def select_four_server(self, server):
        self.wait_and_select_item(self.drpFourServer_xpath, server)

    def set_four_server(self, server):
        self.wait_and_set_text_element_with_delete(self.txtFourServer_xpath, server)

    def get_four_serer(self):
        return self.wait_and_get_selected_text(self.drpFourServer_xpath)

    def click_btn_apply(self):
        self.wait_and_click_element(self.btnApply_xpath)

    def setting_internet_time(self, hostName=None, timezone=None, priSer=None,
                              secSer=None, thirSer=None, fourSer=None, clickApply=False):
        if hostName is not None:
            self.set_hostname(hostName)

        if priSer is not None:
            self.select_pri_server('Other')
            self.set_pri_server(priSer)

        if secSer is not None:
            self.select_sec_server('Other')
            self.set_sec_server(secSer)

        if thirSer is not None:
            self.select_thir_server('Other')
            self.set_thir_server(thirSer)

        if fourSer is not None:
            self.select_four_server('Other')
            self.set_four_server(fourSer)

        if clickApply:
            self.click_btn_apply()

    def get_internet_time(self):
        return [
            self.get_ntp_status(),
            self.get_hostname(),
            'Timezone',
            self.get_pri_serer(),
            self.get_sec_serer(),
            self.get_thir_serer(),
            self.get_four_serer()
        ]

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)


class AdvDiagnosticToolPage(AdvancePage):
    def __init__(self, driver):
        super().__init__(driver)

    txtIPAddr_xpath = "//input[@id='ipaddress']"
    btnPing_xpath = "//input[@onclick='btnApply(1)']"
    btnTrace_xpath = "//input[@onclick='btnApply(0)']"

    def set_ipAddr(self, ipAddr):
        self.wait_and_set_text_element_with_delete(self.txtIPAddr_xpath, ipAddr)

    def click_btn_ping(self):
        self.wait_and_click_element(self.btnPing_xpath)

    def click_btn_trace(self):
        self.wait_and_click_element(self.btnTrace_xpath)

    def setting_diagnostic_tool(self, ipAddr=None, clickPing=True, clickTrace=True):
        if ipAddr is not None:
            self.set_ipAddr(ipAddr)

        if clickPing:
            self.click_btn_ping()

        if clickTrace:
            self.click_btn_trace()

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)


class AdvDDNSPage(AdvancePage):
    def __init__(self, driver):
        super().__init__(driver)

    btnAddDDNS_xpath = "//input[@id='button_add_new']"

    txtEntry_xpath = "//input[@id='add_entry']"
    drpDDNSProvi_xpath = "//select[@id='add_service']"
    txtHostName_xpath = "//input[@id='add_hostname']"
    drpInterface_xpath = "//select[@id='add_interface']"
    txtUserName_xpath = "//input[@id='add_user']"
    txtPassword_xpath = "//input[@id='add_password']"
    btnApply_xpath = "//input[@onclick='ApplyNewDDNS()']"


    def click_add_ddns(self):
        self.wait_and_click_element(self.btnAddDDNS_xpath)

    def navigation_to_add_ddns_page(self):
        self.navigation_to_ddns()
        time.sleep(1)
        self.click_add_ddns()
        time.sleep(1)

    def set_entry(self, dataEntry):
        self.wait_and_set_text_element_with_delete(self.txtEntry_xpath, dataEntry)

    def select_DDNS_Provider(self, ddnsServer):
        self.wait_and_select_item(self.drpDDNSProvi_xpath, ddnsServer)

    def set_hostname(self, hostName):
        self.wait_and_set_text_element_with_delete(self.txtHostName_xpath, hostName)

    def select_Interface(self, interface):
        self.wait_and_select_item(self.drpInterface_xpath, interface)

    def set_userName(self, userName):
        self.wait_and_set_text_element_with_delete(self.txtUserName_xpath, userName)

    def set_password(self, password):
        self.wait_and_set_text_element_with_delete(self.txtPassword_xpath, password)

    def click_apply(self):
        self.wait_and_click_element(self.btnApply_xpath)

    def setting_DDNS(self, dataEnty=None, DDNSServer=None, hostName=None, interface=None,
                     userName=None, password=None, clickApply=False):
        if dataEnty is not None:
            self.set_entry(dataEnty)

        if DDNSServer is not None:
            self.select_DDNS_Provider(DDNSServer)

        if hostName is not None:
            self.set_hostname(hostName)

        if interface is not None:
            self.select_Interface(interface)

        if userName is not None:
            self.set_userName(userName)

        if password is not None:
            self.set_password(password)

        if clickApply:
            self.click_apply()


    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)


class AdvPortForwardPage(AdvancePage):
    def __init__(self, driver):
        super().__init__(driver)

    txtServiceName_xpath = "//input[@id='add_port_name']"
    drpProtocol_xpath = "//select[@id='add_protocol']"
    drpExternalZone_xpath = "//select[@id='add_external_zone']"
    txtExternalPort_xpath = "//input[@id='add_external_port']"
    drpInternalZone_xpath = "//select[@id='add_internal_zone']"
    txtInternalPort_xpath = "//input[@id='add_internal_port']"
    txtInternalIP_xpath = "//input[@id='add_internal_ip']"
    btnAddRule_xpath = "//input[@onclick='btnApply()']"

    btnDelRule_xpath = "//img[@title='Delete rule' and @onclick='DeleteService(%s)']"
    btnEditRule_xpath = "//img[@title='Edit rule' and @onclick='EditService(%s)']"

    def set_service_name(self, serviceName):
        self.wait_and_set_text_element_with_delete(self.txtServiceName_xpath, serviceName)

    def select_protocol(self, protocol):
        self.wait_and_select_item(self.drpProtocol_xpath, protocol)

    def select_external_zone(self, zone):
        self.wait_and_select_item(self.drpExternalZone_xpath, zone)

    def set_external_port(self, port):
        self.wait_and_set_text_element_with_delete(self.txtExternalPort_xpath, port)

    def select_internal_zone(self, zone):
        self.wait_and_select_item(self.drpInternalZone_xpath, zone)

    def set_internal_port(self, port):
        self.wait_and_set_text_element_with_delete(self.txtInternalPort_xpath, port)

    def set_internal_ip(self, ipAddr):
        self.wait_and_set_text_element_with_delete(self.txtInternalIP_xpath, ipAddr)

    def click_btn_add_rule(self):
        self.wait_and_click_element(self.btnAddRule_xpath)

    def setting_port_forward(self, serviceName=None, protocol=None, exZone=None, exPort=None,
                                inZone=None, inPort=None, inIP=None, clickApply=True):
        if serviceName is not None:
            self.set_service_name(serviceName)

        if protocol is not None:
            self.select_protocol(protocol)

        if exZone is not None:
            self.select_external_zone(exZone)

        if exPort is not None:
            self.set_external_port(exPort)

        if inZone is not None:
            self.select_internal_zone(inZone)

        if inPort is not None:
            self.set_internal_port(inPort)

        if inIP is not None:
            self.set_internal_ip(inIP)

        if clickApply:
            self.click_btn_add_rule()


    def edit_port_forward(self, ruleID, protocol=None, exZone=None, exPort=None,
                                inZone=None, inPort=None, inIP=None, clickApply=True):

        self.wait_and_click_element(xpath=(self.btnEditRule_xpath %str(ruleID)))
        if protocol is not None:
            self.wait_and_select_item("//select[@id='edit_protocol']", protocol)

        if exZone is not None:
            self.wait_and_select_item("//select[@id='edit_external_zone']", exZone)

        if exPort is not None:
            self.wait_and_set_text_element_with_delete("//input[@id='edit_external_port']", exPort)

        if inZone is not None:
            self.wait_and_select_item("//select[@id='edit_internal_zone']", inZone)

        if inPort is not None:
            self.wait_and_set_text_element_with_delete("//input[@id='edit_internal_port']", inPort)

        if inIP is not None:
            self.wait_and_set_text_element_with_delete("//input[@id='edit_internal_ip']", inIP)

        if clickApply:
            self.wait_and_click_element("//input[@title='Apply Edit']")

    def delete_port_forward(self, portID):
        self.wait_and_click_element(xpath=(self.btnDelRule_xpath %str(portID)))
        self.accept_alert()

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)


class AdvVlanPage(AdvancePage):
    def __init__(self, driver):
        super().__init__(driver)

    btnAddVlan_xpath = "//input[@onclick='addNewVlan();']"
    txtVlanID_xpath = "//input[@id='input_id_New_Edit']"
    btnApply_xpath = "//input[@onclick='ApplyNew();']"

    def click_add_Vlan(self):
        self.wait_and_click_element(self.btnAddVlan_xpath)

    def set_VLAN_ID(self, vlanID):
        self.wait_and_set_text_element_with_delete(self.txtVlanID_xpath, vlanID)

    def click_apply(self):
        self.wait_and_click_element(self.btnApply_xpath)

    def nagigate_to_vlan_setting(self):
        self.navigation_to_VLAN()
        time.sleep(1)
        self.click_add_Vlan()
        time.sleep(1)

    def setting_vlan(self, vlanID=None, clickApply=False):
        if vlanID is not None:
            self.set_VLAN_ID(vlanID)

        if clickApply:
            self.click_apply()

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)


class AdvFirewallPage(AdvancePage):
    def __init__(self, driver):
        super().__init__(driver)

    btnAddVlan_xpath = "//input[@onclick='addNewFirewallZone();']"
    txtZoneName_xpath = "//input[@id='edit_zone_name']"
    btnApplyAdd_xpath = "//input[@id='apply_add']"

    def click_btn_add_vlan(self):
        self.wait_and_click_element(self.btnAddVlan_xpath)

    def set_zone_name(self, zoneName):
        self.wait_and_set_text_element_with_delete(self.txtZoneName_xpath, zoneName)

    def click_btn_apply_add(self):
        self.wait_and_click_element(self.btnApplyAdd_xpath)

    def navigate_to_new_firewall_setting(self):
        self.navigation_to_firewall()
        time.sleep(1)
        self.click_btn_add_vlan()
        time.sleep(1)

    def navigate_to_edit_firewall_setting(self):
        self.navigation_to_firewall()
        time.sleep(1)
        self.click_btn_add_vlan()
        time.sleep(1)

    def setting_new_firewall(self, zoneName=None, clickApply=False):
        if zoneName is not None:
            self.set_zone_name(zoneName)

        if clickApply:
            self.click_btn_apply_add()

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)

class AdvRouteSetPage(AdvancePage):
    def __init__(self, driver):
        super().__init__(driver)

    btnAddRoute_xpath = "//input[@onclick='AddNewRoute();']"
    drpInterface_xpath = "//select[@id='route_interface']"
    txtIPv4Target_xpath = "//input[@id='route_target']"
    txtIPv4Netmask_xpath = "//input[@id='route_netmask']"
    txtIPv4Gateway_xpath = "//input[@id='route_gateway']"
    txtMetric_xpath = "//input[@id='route_metric']"
    txtMTU_xpath = "//input[@id='route_mtu']"
    btnApplyAdd_xpath = "//input[@id='apply_add']"

    def click_btn_add_route(self):
        self.wait_and_click_element(self.btnAddRoute_xpath)

    def select_interface(self, interface):
        self.wait_and_select_item(self.drpInterface_xpath, interface)

    def set_ipv4_addr(self, ipAddr):
        self.wait_and_set_text_element_with_delete(self.txtIPv4Target_xpath, ipAddr)

    def set_ipv4_netmask(self, netmask):
        self.wait_and_set_text_element_with_delete(self.txtIPv4Netmask_xpath, netmask)

    def set_ipv4_gateway(self, gateway):
        self.wait_and_set_text_element_with_delete(self.txtIPv4Gateway_xpath, gateway)

    def set_metric(self, metric):
        self.wait_and_set_text_element_with_delete(self.txtMetric_xpath, metric)

    def set_mtu(self, mtu):
        self.wait_and_set_text_element_with_delete(self.txtMTU_xpath, mtu)

    def click_btn_apply_add(self):
        self.wait_and_click_element(self.btnApplyAdd_xpath)

    def navigate_to_add_route_page(self):
        self.navigation_to_route()
        time.sleep(1)
        self.click_btn_add_route()
        time.sleep(1)

    def setting_new_route(self, interface=None, ipAddr=None, netmask=None,
                          gateway=None, metric=None, mtu=None, clickApply=False):
        if interface is not None:
            self.select_interface(interface)

        if ipAddr is not None:
            self.set_ipv4_addr(ipAddr)

        if netmask is not None:
            self.set_ipv4_netmask(netmask)

        if gateway is not None:
            self.set_ipv4_gateway(gateway)

        if metric is not None:
            self.set_metric(metric)

        if mtu is not None:
            self.set_mtu(mtu)

        if clickApply:
            self.click_btn_apply_add()

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)