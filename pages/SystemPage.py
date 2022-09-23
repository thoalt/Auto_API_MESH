import time

from base.WEBLib import Web_Lib

class SystemPage(Web_Lib):
    lnkSystemTab_xpath = "//a[@title='System']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_system_tab(self):
        self.wait_and_click_element(self.lnkSystemTab_xpath)


class SystemDevInfoPage(SystemPage):
    def __init__(self, driver):
        super().__init__(driver)

    lnkDeviceIfoTab_xpath = "//a[@id='titledevice']"
    lnkClientMonitor_xpath = "//img[@id='stationDown']"
    lnkClientSetting_xpath = "//a[@id='sub133']"

    txtAccountInterval_xpath = "//input[@id='AccountingInterval']"
    txtStoredPeriod_xpath = "//input[@id='StoredPeriods']"
    drpSaveInterval_xpath = "//select[@id='CommitInterval']"
    drpRefreshInterval_xpath = "//select[@id='RefreshInterval']"

    btnApply_xpath = "//input[@onclick='SetStationSetting();']"

    def click_device_infor_tab(self):
        self.wait_and_click_element(self.lnkDeviceIfoTab_xpath)

    def click_client_monitor(self):
        self.wait_and_click_element(self.lnkClientMonitor_xpath)

    def click_client_setting(self):
        self.wait_and_click_element(self.lnkClientSetting_xpath)

    def set_account_interval(self, accounInterval):
        self.wait_and_set_text_element_with_delete(self.txtAccountInterval_xpath, accounInterval)

    def get_account_interval(self):
        return self.wait_and_get_attribute_element(self.txtAccountInterval_xpath, 'value')

    def set_store_period(self, storePeriod):
        self.wait_and_set_text_element_with_delete(self.txtStoredPeriod_xpath, storePeriod)

    def get_store_period(self):
        return self.wait_and_get_attribute_element(self.txtStoredPeriod_xpath, 'value')

    def get_save_interval(self):
        return self.wait_and_get_selected_text(self.drpSaveInterval_xpath)

    def get_refresh_interval(self):
        return self.wait_and_get_selected_text(self.drpRefreshInterval_xpath)

    def click_btn_apply(self):
        self.wait_and_click_element(self.btnApply_xpath)

    def navigation_to_client_monitoring(self):
        self.click_system_tab()
        self.click_device_infor_tab()
        self.click_client_monitor()
        self.click_client_setting()

    def setting_client_moniotring(self, accInterval=None, storePeriod=None, clickApply=True):
        if accInterval is not None:
            self.set_account_interval(accInterval)

        if storePeriod is not None:
            self.set_store_period(storePeriod)

        if clickApply:
            self.click_btn_apply()

    def get_client_monitoring(self):
        return [
            self.get_account_interval(),
            self.get_store_period(),
            self.get_save_interval(),
            self.get_refresh_interval()
        ]
    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)

class SystemManagerPage(SystemPage):
    def __init__(self, driver):
        super().__init__(driver)

    lnkManagerTab_xpath = "//a[@id='titlemanagement']"
    lnkAdminTab_xpath = "//a[@id='sub35']"
    txtOldPass_xpath = "//input[@id='Text_OLD_PWD']"
    txtNewPass_xpath = "//input[@id='Text_NEW_PWD']"
    txtConfirmPass_xpath = "//input[@id='Text_CFM_NEW_PWD']"
    lbOldPass_xpath = "//td[contains(text(),'Old Password')]"
    btnUpdatePass_xpath = "//input[@id='BTN_UpdatePWD']"

    lnkUMPTab_xpath = "//a[@id='sub36']"
    lnkSerConfTab_xpath = "//a[@id='sub361']"
    drpInterface_xpath = "//select[@id='Select_Interface']"
    txtUmpUser_xpath = "//input[@id='add_user']"
    txtUmpPass_xpath = "//input[@id='add_password']"
    txtUmpPeriodic_xpath = "//input[@id='add_interval']"
    drpPeriodicStatus = "//select[@id='Select_Enable']"
    lbSerConf_xpath = "//td[contains(text(),'Server Configuration')]"
    btnApply_xpath = "//input[@onclick='SetEasyCWMP()']"

    lnkAlarmConfTab_xpath = "//a[@id='sub362']"
    drpReboot_xpath = "//select[@id='reboot']"
    drpchange_fw_version_xpath = "//select[@id='change_fw_version']"
    drpcpu_usage_over_threshold_xpath = "//select[@id='cpu_usage_over_threshold']"
    drpram_usage_over_threshold_xpath = "//select[@id='ram_usage_over_threshold']"
    drpremain_low_disk_space_xpath = "//select[@id='remain_low_disk_space']"
    drpdownload_fw_error_xpath = "//select[@id='download_fw_error']"
    drpapply_fw_error_xpath = "//select[@id='apply_fw_error']"
    drpchange_wan_ip_xpath = "//select[@id='change_wan_ip']"



    def click_manager_tab(self):
        self.wait_and_click_element(self.lnkManagerTab_xpath)

    def click_admin_tab(self):
        self.wait_and_click_element(self.lnkAdminTab_xpath)

    def click_UMP_tab(self):
        self.wait_and_click_element(self.lnkUMPTab_xpath)

    def click_server_conf_tab(self):
        self.wait_and_click_element(self.lnkSerConfTab_xpath)

    def click_alarm_conf_tab(self):
        self.wait_and_click_element(self.lnkAlarmConfTab_xpath)

    def select_interface(self, interface):
        self.wait_and_select_item(self.drpInterface_xpath, interface)

    def get_UMP_interface(self):
        return self.wait_and_get_selected_text(self.drpInterface_xpath)

    def set_admin_old_pass(self, oldPass):
        #self.wait_and_set_text_element_with_delete(self.txtOldPass_xpath, oldPass)
        self.wait_and_set_text_element_without_enter(self.txtOldPass_xpath, oldPass)
        self.wait_and_click_element(self.lbOldPass_xpath)

    def set_admin_new_pass(self, newPass):
        #self.wait_and_set_text_element_with_delete(self.txtNewPass_xpath, newPass)
        self.wait_and_set_text_element_without_enter(self.txtNewPass_xpath, newPass)
        self.wait_and_click_element(self.lbOldPass_xpath)

    def set_admin_confrim_pass(self, confirmPass):
        #self.wait_and_set_text_element_with_delete(self.txtConfirmPass_xpath, confirmPass)
        self.wait_and_set_text_element_without_enter(self.txtConfirmPass_xpath, confirmPass)
        self.wait_and_click_element(self.lbOldPass_xpath)

    def click_update_pass(self):
        self.wait_and_click_element(self.btnUpdatePass_xpath)

    def set_Ump_user(self, UmpUser):
        self.wait_and_set_text_element_with_delete(self.txtUmpUser_xpath, UmpUser)

    def get_ump_user(self):
        return self.wait_and_get_attribute_element(self.txtUmpUser_xpath, 'value')

    def set_Ump_password(self, UmpPass):
        self.wait_and_set_text_element_with_delete(self.txtUmpPass_xpath, UmpPass)

    def get_ump_password(self):
        return self.wait_and_get_attribute_element(self.txtUmpPass_xpath, 'value')

    def get_ump_periodic_status(self):
        return self.wait_and_get_selected_text(self.drpPeriodicStatus)

    def set_Ump_periodic(self, UmpPeriodic):
        self.wait_and_set_text_element_with_delete(self.txtUmpPeriodic_xpath, UmpPeriodic)

    def get_ump_periodic(self):
        return self.wait_and_get_attribute_element(self.txtUmpPeriodic_xpath, 'value')

    def get_reboot(self):
        return
    def click_btn_apply(self):
        self.wait_and_click_element(self.btnApply_xpath)

    def navigate_to_administrator_page(self):
        self.click_system_tab()
        self.click_manager_tab()
        time.sleep(1)
        self.click_admin_tab()
        time.sleep(2)

    def navigation_to_server_config_page(self):
        self.click_system_tab()
        self.click_manager_tab()
        time.sleep(1)
        self.click_UMP_tab()
        time.sleep(1)
        self.click_server_conf_tab()
        time.sleep(2)

    def navigation_to_alarm_config_page(self):
        self.click_system_tab()
        self.click_manager_tab()
        time.sleep(1)
        self.click_UMP_tab()
        time.sleep(1)
        self.click_alarm_conf_tab()
        time.sleep(2)

    def change_admin_pass(self, oldPass=None, newPass=None, confirmPass=None, clickBtnUpdate=True):
        if oldPass is not None:
            self.set_admin_old_pass(oldPass)

        if newPass is not None:
            self.set_admin_new_pass(newPass)

        if confirmPass is not None:
            self.set_admin_confrim_pass(confirmPass)

        if clickBtnUpdate:
            self.click_update_pass()

    def setting_server_configuration(self, interface=None, user=None, password=None, perInteval=None, clickApply=True):
        if interface is not None:
            self.select_interface(interface)

        if user is not None:
            self.set_Ump_user(user)

        if password is not None:
            self.set_Ump_password(password)

        if perInteval is not None:
            self.set_Ump_periodic(perInteval)

        if clickApply:
            self.click_btn_apply()

    def get_server_configuration(self):
        return [self.get_UMP_interface(),
                self.get_ump_user(),
                self.get_ump_password(),
                self.get_ump_periodic_status(),
                self.get_ump_periodic(),
                self.get_UMP_interface()]

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)