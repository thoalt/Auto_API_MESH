import time
from dataclasses import dataclass

from base.WEBLib import Web_Lib


@dataclass
class RadioInfo_EW12STv1:
    status: bool
    standard: str
    channel: str
    bandwith: str
    power: int
    countryCode: str

@dataclass
class RadioInfo_EW12STv2:
    status: bool
    standard: str
    channel: str
    bandwith: str
    power: int
    countryCode: str
    channelOptimize: str

@dataclass
class SSID_Info:
    ssidName: str
    serMode: str
    password: str

@dataclass
class GUES_SSID_Info:
    status: str
    ssidName: str
    serMode: str
    password: str

@dataclass
class REPEATER_Info:
    status: str
    ssidName: str
    serMode: str
    password: str

class WIFI_TYPE():
    T_24G = "2G"
    T_5G = '5G'

class STANDARD_2G():
    MOD_G = '11g'
    MOD_NG = '11ng'

class STANDARD_5G():
    MOD_A = '11a'
    MOD_NA = '11na'
    MOD_AC = '11ac'


class CHANNEL_GUI():
    C_AUTO = "Auto"
    C_1 = "1"
    C_2 = "2"
    C_3 = "3"
    C_4 = "4"
    C_5 = "5"
    C_6 = "6"
    C_7 = "7"
    C_8 = "8"
    C_9 = "9"
    C_10 = "10"
    C_11 = "11"
    C_36 = "36"
    C_40 = "40"
    C_44 = "44"
    C_48 = "48"
    C_52 = "52"
    C_56 = "56"
    C_60 = "60"
    C_64 = "64"
    C_100 = "100"
    C_104 = "104"
    C_112 = "112"
    C_116 = "116"
    C_120 = "120"
    C_124 = "124"
    C_128 = "128"
    C_132 = "132"
    C_136 = "136"
    C_140 = "140"
    C_144 = "144"
    C_149 = "149"
    C_153 = "153"
    C_157 = "157"
    C_161 = "161"
    C_165 = "165"

class BAND_WITH_GUI():
    B_20 = "20 MHz"
    B_40 = "40 MHz"
    B_20_40 = "20/40 MHz"
    B_80 = "80 MHz"

class WirelessPage(Web_Lib):
    def __init__(self, driver):
        super().__init__(driver)

    lnkSettingCap_xpath = "//a[@id='titleSettingCap']"
    lnkWireless_xpath = "//a[@id='titlewlancap']"
    lnkRadio_xpath = "//a[@id='sub61']"
    lnkSSID_xpath = "//a[@id='sub62']"
    lnkGuestSSID_xpath = "//a[@id='sub64']"
    lnkRepeater_xpath = "//a[@id='sub63']"

    def click_Setting_Cap(self):
        self.wait_and_click_element(self.lnkSettingCap_xpath)

    def click_Wireless(self):
        self.wait_and_click_element(self.lnkWireless_xpath)

    def click_Radio(self):
        self.wait_and_click_element(self.lnkRadio_xpath)

    def click_SSID(self):
        self.wait_and_click_element(self.lnkSSID_xpath)

    def click_GuestSSID(self):
        self.wait_and_click_element(self.lnkGuestSSID_xpath)

    def click_Repeater(self):
        self.wait_and_click_element(self.lnkRepeater_xpath)


class WirelessRadioPage(WirelessPage):
    def __init__(self, driver):
        super().__init__(driver)

    lnkRadio2G_xpath = "//li[@id='menu_basic']"
    btnEditRadio2G_xpath = "//input[@id='EditRadio2']"
    lbRadio2G_xpath = "//td[contains(text(),'Radio 2.4 GHz Setting')]"
    drpStatus2G_xpath = "//select[@id='2G_Select_Status']"
    drpStandard2G_xpath = "//select[@id='2G_Select_WLAN_Mode']"
    drpChannel2G_xpath = "//select[@id='2G_Select_Channel']"
    drpBandwith2G_xpath = "//select[@id='2G_Select_Bandwidth']"
    txtPower2G_xpath = "//input[@id='2G_Select_TX_Power']"
    drpCountryCode2G_xpath = "//select[@id='2G_Select_Country']"
    drpChannelOptimize2G_xpath = "//select[@id='2G_Select_Channel_Optimization']"
    btnApply2G_xpath = "//input[@id='buttonApply2G']"

    lnkRadio5G_xpath = "//li[@id='menu_advance']"
    btnEditRadio5G_xpath = "//input[@id='EditRadio5']"
    lbRadio5G_xpath = "//td[contains(text(),'Radio 5 GHz Setting')]"
    drpStatus5G_xpath = "//select[@id='5G_Select_Status']"
    drpStandard5G_xpath = "//select[@id='5G_Select_WLAN_Mode']"
    drpChannel5G_xpath = "//select[@id='5G_Select_Channel']"
    drpBandwith5G_xpath = "//select[@id='5G_Select_Bandwidth']"
    txtPower5G_xpath = "//input[@id='5G_Select_TX_Power']"
    drpCountryCode5G_xpath = "//select[@id='5G_Select_Country']"
    drpChannelOptimize5G_xpath = "//select[@id='5G_Select_Channel_Optimization']"
    btnApply5G_xpath = "//input[@id='buttonApply5G']"

    ## Label to get information
    lbPower_xpath = "//label[@id='txpower']"
    lbChannel_xpath = "//label[@id='channel']"
    lbCountryCode_xpath = "//label[@id='country_code']"

    def click_Radio2G(self):
        self.wait_and_click_element(self.lnkRadio2G_xpath)

    def click_Btn_Edit_Radio2G(self):
        self.wait_and_click_element(self.btnEditRadio2G_xpath)

    def get_Status2G(self):
        return self.wait_and_get_selected_text(self.drpStatus2G_xpath)

    def select_Standard2G(self, standard):
        self.wait_and_select_item(self.drpStandard2G_xpath, standard)

    def get_Standard2G_sp(self):
        return self.wait_and_get_selected_text(self.drpStandard2G_xpath)

    def select_Channel2G(self, channel):
        self.wait_and_select_item(self.drpChannel2G_xpath, channel)

    def get_Channel2G_sp(self):
        return self.wait_and_get_selected_text(self.drpChannel2G_xpath)

    def select_Bandwith2G(self, bandwith):
        self.wait_and_select_item(self.drpBandwith2G_xpath, bandwith)

    def get_Bandwith2G_sp(self):
        return self.wait_and_get_selected_text(self.drpBandwith2G_xpath)

    def set_TxPower2G(self, txPower):
        self.wait_and_set_text_element_with_delete(self.txtPower2G_xpath, txPower)

    def get_TxPower2G_sp(self):
        return self.wait_and_get_attribute_element(self.txtPower2G_xpath, 'value')

    def get_CountryCode2G_sp(self):
        return self.wait_and_get_attribute_element(self.drpCountryCode2G_xpath, 'value')

    def get_ChannelOptimize2G_sp(self):
        return self.wait_and_get_selected_text(self.drpChannelOptimize2G_xpath)

    def click_BtnApply_Radio2G(self):
        self.wait_and_click_element(self.btnApply2G_xpath)

    # Get info in Overview Page
    def get_TxPower2G(self):
        return self.wait_and_get_text_element(self.lbPower_xpath)

    def get_Channel2G(self):
        return self.wait_and_get_text_element(self.lbChannel_xpath)

    def get_CountryCode2G(self):
        return self.wait_and_get_text_element(self.lbCountryCode_xpath)

    ### Setting Radio 5G
    def click_Radio5G(self):
        self.wait_and_click_element(self.lnkRadio5G_xpath)

    def click_Btn_Edit_Radio5G(self):
        self.wait_and_click_element(self.btnEditRadio5G_xpath)

    def get_status5G(self):
        return self.wait_and_get_selected_item(self.drpStatus5G_xpath)

    def select_Standard5G(self, standard):
        self.wait_and_select_item(self.drpStandard5G_xpath, standard)

    def get_Standard5G_sp(self):
        return self.wait_and_get_selected_text(self.drpStandard5G_xpath)

    def select_Channel5G(self, channel):
        self.wait_and_select_item(self.drpChannel5G_xpath, channel)

    def get_Channel5G_sp(self):
        return self.wait_and_get_selected_text(self.drpChannel5G_xpath)

    def select_Bandwith5G(self, bandwith):
        self.wait_and_select_item(self.drpBandwith5G_xpath, bandwith)

    def get_Bandwith5G_sp(self):
        return self.wait_and_get_selected_text(self.drpBandwith5G_xpath)

    def set_TxPower5G(self, txPower):
        self.wait_and_set_text_element_with_delete(self.txtPower5G_xpath, txPower)

    def get_TxPower5G_sp(self):
        return self.wait_and_get_attribute_element(self.txtPower5G_xpath, 'value')

    def get_CountryCode5G_sp(self):
        return self.wait_and_get_attribute_element(self.drpCountryCode5G_xpath, 'value')

    def get_ChannelOptimize5G_sp(self):
        return self.wait_and_get_selected_text(self.drpChannelOptimize5G_xpath)

    def click_Btn_Apply_Radio5G(self):
        self.wait_and_click_element(self.btnApply5G_xpath)

    # Get infor in Oveview page
    def get_TxPower5G(self):
        return self.wait_and_get_text_element(self.lbPower_xpath)

    def get_Channel5G(self):
        return self.wait_and_get_text_element(self.lbChannel_xpath)

    def get_CountryCode5G(self):
        return self.wait_and_get_text_element(self.lbCountryCode_xpath)

    def navigate_to_radio_2G_page(self):
        self.click_Setting_Cap()
        self.click_Wireless()
        time.sleep(1)
        self.click_Radio()
        time.sleep(1)
        self.click_Radio2G()
        time.sleep(1)

    def navigate_to_radio_2G_setting_page(self):
        self.navigate_to_radio_2G_page()
        self.click_Btn_Edit_Radio2G()
        time.sleep(1)

    def navigate_to_radio_5G_page(self):
        self.click_Setting_Cap()
        self.click_Wireless()
        time.sleep(1)
        self.click_Radio()
        time.sleep(1)
        self.click_Radio5G()
        time.sleep(1)

    def navigate_to_radio_5G_setting_page(self):
        self.navigate_to_radio_5G_page()
        self.click_Btn_Edit_Radio5G()
        time.sleep(1)

    def setting_Radio(self, bandW=None, standard=None, channel=None, bandwith=None, txPower=None, clickApply=True):
        if bandW == '2G':
            if standard is not None:
                self.select_Standard2G(standard)

            if channel is not None:
                self.select_Channel2G(channel)

            if bandwith is not None:
                self.select_Bandwith2G(bandwith)

            if txPower is not None:
                self.set_TxPower2G(txPower)

            if clickApply:
                self.click_BtnApply_Radio2G()

        elif bandW == '5G':
            if standard is not None:
                self.select_Standard5G(standard)

            if channel is not None:
                self.select_Channel5G(channel)

            if bandwith is not None:
                self.select_Bandwith5G(bandwith)

            if txPower is not None:
                self.set_TxPower5G(txPower)

            if clickApply:
                self.click_Btn_Apply_Radio5G()
        else:
            raise ("Invalid Bandwidth Setting!")

    def get_Radio_Overview_2G(self):
        return [
            "MAC Addr",
            self.get_Channel2G(),
            self.get_TxPower2G(),
            self.get_CountryCode2G()
        ]

    def get_Radio_Overview_5G(self):
        return [
            "MAC Addr",
            self.get_Channel5G(),
            self.get_TxPower5G(),
            self.get_CountryCode5G()
        ]

    def get_Radio_Infor_2G(self, type):
        if type == "EW12_STv1":
            return RadioInfo_EW12STv1(
                self.get_Status2G(),
                self.get_Standard2G_sp(),
                self.get_Channel2G_sp(),
                self.get_Bandwith2G_sp(),
                self.get_TxPower2G_sp(),
                self.get_CountryCode2G_sp()
            )
        else:
            return RadioInfo_EW12STv2(
                self.get_Status2G(),
                self.get_Standard2G_sp(),
                self.get_Channel2G_sp(),
                self.get_Bandwith2G_sp(),
                self.get_TxPower2G_sp(),
                self.get_CountryCode2G_sp(),
                self.get_ChannelOptimize2G_sp()
            )

    def get_Radio_Infor_5G(self, type):
        if type == "EW12_STv1":
            return RadioInfo_EW12STv1(
                self.get_status5G(),
                self.get_Standard5G_sp(),
                self.get_Channel5G_sp(),
                self.get_Bandwith5G_sp(),
                self.get_TxPower5G_sp(),
                self.get_CountryCode5G_sp()
            )
        else:
            return RadioInfo_EW12STv2(
                self.get_status5G(),
                self.get_Standard5G_sp(),
                self.get_Channel5G_sp(),
                self.get_Bandwith5G_sp(),
                self.get_TxPower5G_sp(),
                self.get_CountryCode5G_sp(),
                self.get_ChannelOptimize5G_sp()
            )

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)


class WirelessSSDIPage(WirelessPage):
    def __init__(self, driver):
        super().__init__(driver)

    lbSSIDConfig_xpath = "//td[contains(text(),'SSID Configuration')]"
    txtSSID_xpath = "//input[@id='Input_SSID']"
    drpNetAuth_xpath = "//select[@id='Select_Security_Mode']"
    txtWPAPass_xpath = "//input[@id='Input_WPA_passphrase']"
    btnApplySSID_xpath = "//input[@id='button_ApplySSID']"

    def set_SSID(self, SSIDName):
        self.wait_and_set_text_element_with_delete(self.txtSSID_xpath, SSIDName)

    def get_SSID(self):
        return  self.wait_and_get_attribute_element(self.txtSSID_xpath, attribute_name='value')

    def select_Net_Authen(self, netAuthen):
        self.wait_and_select_item(self.drpNetAuth_xpath, netAuthen)

    def get_Authen(self):
        return self.wait_and_get_selected_text(self.drpNetAuth_xpath)

    def set_WPA_Pass(self, wpaPass):
        self.wait_and_set_text_element_with_delete(self.txtWPAPass_xpath, wpaPass)

    def get_WPA_Pass(self):
        return self.wait_and_get_attribute_element(self.txtWPAPass_xpath, attribute_name='value')

    def click_Btn_Apply_SSID(self):
        self.wait_and_click_element(self.btnApplySSID_xpath)

    def navigation_to_SSID_page(self):
        self.click_Setting_Cap()
        self.click_Wireless()
        time.sleep(1)
        self.click_SSID()
        time.sleep(1)

    def setting_SSID_config(self, SSID=None, WSecurity=None, password=None, clickApply=True):
        if SSID is not None:
            self.set_SSID(SSID)

        if WSecurity is not None:
            self.select_Net_Authen(WSecurity)

        if password is not None:
            self.set_WPA_Pass(password)

        if clickApply:
            self.click_Btn_Apply_SSID()

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)

    def Get_SSID_Info(self):
        ssid = self.get_SSID()
        authen = self.get_Authen()

        if authen != "OPEN":
            wpa_pass = self.get_WPA_Pass()
        else:
            wpa_pass = ''
        return SSID_Info(
            ssid,
            authen,
            wpa_pass
        )

class WirelessGuestSSDIPage(WirelessPage):
    def __init__(self, driver):
        super().__init__(driver)

    lnkGuest2G_xpath = "//a[contains(text(),'Guest 2.4 GHz')]"
    lbGuest2G_xpath = "//td[contains(text(),'2.4 GHz Guest')]"
    cbkEnableGuest2G_xpath = "//input[@id='enable_guest_2g']"
    txtGuest2G_SSID_xpath = "//input[@id='Input_SSID']"
    drtGuest2G_NetAuth_xpath = "//select[@id='Select_Network_Authen']"
    txtGuest2G_WPAPass_xpath = "//input[@id='Input_WPA_passphrase']"
    btnGuest2G_ApplySSID_xpath = "//input[@id='button_ApplyGuest2G']"

    lnkGuest5G_xpath = "//a[contains(text(),'Guest 5 GHz')]"
    lbGuest5G_xpath = "//td[contains(text(),'5 GHz Guest')]"
    cbkEnableGuest5G_xpath = "//input[@id='5G_Enable_Guest']"
    txtGuest5G_SSID_xpath = "//input[@id='5G_Input_SSID']"
    drtGuest5G_NetAuth_xpath = "//select[@id='5G_Select_Network_Authen']"
    txtGuest5G_WPAPass_xpath = "//input[@id='5G_Input_WPA_passphrase']"
    btnGuest5G_ApplySSID_xpath = "//input[@id='button_ApplyGuest5G']"

    def click_Guest2G(self):
        self.wait_and_click_element(self.lnkGuest2G_xpath)

    def check_Enable_Guest2G(self):
        self.wait_and_check_checkbox(self.cbkEnableGuest2G_xpath)

    def get_Enable_Guest2G_status(self):
        return self.wait_and_get_checkbox_selected(self.cbkEnableGuest2G_xpath)

    def set_SSID_Guest2G(self, SSIDName):
        self.wait_and_set_text_element_with_delete(self.txtGuest2G_SSID_xpath, SSIDName)

    def getSSID_Guest2G(self):
        return self.wait_and_get_attribute_element(self.txtGuest2G_SSID_xpath, attribute_name='value')

    def select_NetAuthen_Guest2G(self, netAuthen):
        self.wait_and_select_item(self.drtGuest2G_NetAuth_xpath, netAuthen)

    def get_NetAuthen_Guest2G(self):
        return self.wait_and_get_selected_text(self.drtGuest2G_NetAuth_xpath)

    def set_WPAPass_Guest2G(self, wpaPass):
        self.wait_and_set_text_element_with_delete(self.txtGuest2G_WPAPass_xpath, wpaPass)

    def get_WPAPass_Guest2G(self):
        return self.wait_and_get_attribute_element(self.txtGuest2G_WPAPass_xpath, attribute_name='value')

    def click_Btn_Apply_Guest2G(self):
        self.wait_and_click_element(self.btnGuest2G_ApplySSID_xpath)

    def click_Guest5G(self):
        self.wait_and_click_element(self.lnkGuest5G_xpath)

    def check_Enable_Guest5G(self):
        self.wait_and_check_checkbox(self.cbkEnableGuest5G_xpath)

    def get_Enable_Guest5G_status(self):
        return self.wait_and_get_checkbox_selected(self.cbkEnableGuest5G_xpath)

    def set_SSID_Guest5G(self, SSIDName):
        self.wait_and_set_text_element_with_delete(self.txtGuest5G_SSID_xpath, SSIDName)

    def getSSID_Guest5G(self):
        return self.wait_and_get_attribute_element(self.txtGuest5G_SSID_xpath, attribute_name='value')

    def select_NetAuthen_Guest5G(self, netAuthen):
        self.wait_and_select_item(self.drtGuest5G_NetAuth_xpath, netAuthen)

    def get_NetAuthen_Guest5G(self):
        return self.wait_and_get_selected_text(self.drtGuest5G_NetAuth_xpath)

    def set_WPAPass_Guest5G(self, wpaPass):
        self.wait_and_set_text_element_with_delete(self.txtGuest5G_WPAPass_xpath, wpaPass)

    def get_WPAPass_Guest5G(self):
        return self.wait_and_get_attribute_element(self.txtGuest5G_WPAPass_xpath, attribute_name='value')

    def click_Btn_Apply_Guest5G(self):
        self.wait_and_click_element(self.btnGuest5G_ApplySSID_xpath)

    def navigation_to_Guest_SSID_setting_page(self):
        self.click_Setting_Cap()
        self.click_Wireless()
        time.sleep(1)
        self.click_GuestSSID()
        time.sleep(1)

    def setting_Guest(self, bandMode=None, enbaleCb=False, SSID=None, WSecurity=None, password=None, clickApply=True):
        if bandMode == '2G':
            self.click_Guest2G()
            time.sleep(1)

            if enbaleCb == True:
                self.check_Enable_Guest2G()

            if SSID is not None:
                self.set_SSID_Guest2G(SSID)

            if WSecurity is not None:
                self.select_NetAuthen_Guest2G(WSecurity)

            if password is not None:
                self.set_WPAPass_Guest2G(password)

            if clickApply:
                self.click_Btn_Apply_Guest2G()

        elif bandMode == '5G':
            self.click_Guest5G()
            time.sleep(1)

            if enbaleCb == True:
                self.check_Enable_Guest5G()

            if SSID is not None:
                self.set_SSID_Guest5G(SSID)

            if WSecurity is not None:
                self.select_NetAuthen_Guest5G(WSecurity)

            if password is not None:
                self.set_WPAPass_Guest5G(password)

            if clickApply:
                self.click_Btn_Apply_Guest5G()

    def Get_GuestSSID_Infor(self, bandMode):
        if bandMode == '5G':
            self.click_Guest5G()
            time.sleep(1)

            status = self.get_Enable_Guest5G_status()

            if status == True:
                netAuth = self.get_NetAuthen_Guest5G()
                print(netAuth)
                ssid = self.getSSID_Guest5G()
                if netAuth != "OPEN":
                    passW = self.get_WPAPass_Guest5G()
                    return GUES_SSID_Info(
                        status=status,
                        ssidName=ssid,
                        serMode=netAuth,
                        password=passW
                    )
                else:
                    return GUES_SSID_Info(
                        status=status,
                        ssidName=ssid,
                        serMode=netAuth,
                        password=''
                    )
            else:
                status = self.get_Enable_Guest5G_status()
                return GUES_SSID_Info(
                    status=status,
                    ssidName='',
                    serMode='',
                    password=''
                )
        elif bandMode == '2G':
            self.click_Guest2G()
            time.sleep(1)

            status = self.get_Enable_Guest2G_status()

            if status == True:
                netAuth = self.get_NetAuthen_Guest2G()
                print(netAuth)
                ssid = self.getSSID_Guest2G()
                if netAuth != "OPEN":
                    passW = self.get_WPAPass_Guest2G()
                    return GUES_SSID_Info(
                        status=status,
                        ssidName=ssid,
                        serMode=netAuth,
                        password=passW
                    )
                else:
                    return GUES_SSID_Info(
                        status=status,
                        ssidName=ssid,
                        serMode=netAuth,
                        password=''
                    )
            else:
                status = self.get_Enable_Guest2G_status()
                return GUES_SSID_Info(
                    status=status,
                    ssidName='',
                    serMode='',
                    password=''
                )

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)

class WirelessRepeaterIPage(WirelessPage):
    def __init__(self, driver):
        super().__init__(driver)

    lnkRepeat2G_xpath = "//a[contains(text(),'Repeater 2.4 GHz')]"
    lbRepeat2G_xpath = "//td[contains(text(),'2.4 GHz Repeater')]"
    cbkEnableRepeat2G_xpath = "//input[@id='enable_repeater_2g']"
    txtRepeat2G_SSID_xpath = "//input[@id='Input_SSID']"
    txtRepeat2G_BSSID_xpath = "//input[@id='Input_BSSID']"
    drtRepeat2G_NetAuth_xpath = "//select[@id='Select_Network_Authen']"
    txtRepeat2G_WPAPass_xpath = "//input[@id='Input_WPA_passphrase']"
    btnRepeat2G_ApplySSID_xpath = "//input[@id='button_ApplyRepeater2G']"

    lnkRepeat5G_xpath = "//a[contains(text(),'Repeater 5 GHz')]"
    lbRepeat5G_xpath = "//td[contains(text(),'5 GHz Repeater')]"
    cbkEnableRepeat5G_xpath = "//input[@id='5G_Enable_Repeater']"
    txtRepeat5G_SSID_xpath = "//input[@id='5G_Input_SSID']"
    txtRepeat5G_BSSID_xpath = "//input[@id='5G_Input_BSSID']"
    drtRepeat5G_NetAuth_xpath = "//select[@id='5G_Select_Network_Authen']"
    txtRepeat5G_WPAPass_xpath = "//input[@id='5G_Input_WPA_passphrase']"
    btnRepeat5G_ApplySSID_xpath = "//input[@id='5G_Input_WPA_passphrase']"

    def click_Repeat2G(self):
        self.wait_and_click_element(self.lnkRepeat2G_xpath)

    def check_Enable_Repeat2G(self):
        self.wait_and_check_checkbox(self.cbkEnableRepeat2G_xpath)

    def get_Enable_Repeat2G_status(self):
        return self.wait_and_get_checkbox_selected(self.cbkEnableRepeat2G_xpath)

    def set_SSID_Repeat2G(self, SSIDName):
        self.wait_and_set_text_element_with_delete(self.txtRepeat2G_SSID_xpath,  SSIDName)

    def get_SSID_Repeat2G(self):
        return self.wait_and_get_attribute_element(self.txtRepeat2G_SSID_xpath, attribute_name='value')

    def set_BSSID_Repeat2G(self, BSSIDName):
        self.wait_and_set_text_element_with_delete(self.txtRepeat2G_BSSID_xpath, BSSIDName)

    def select_NetAuthen_Repeat2G(self, netAuthen):
        self.wait_and_select_item(self.drtRepeat2G_NetAuth_xpath, netAuthen)

    def get_NetAuthen_Repeat2G(self):
        return self.wait_and_get_selected_text(self.drtRepeat2G_NetAuth_xpath)

    def set_WPAPass_Repeat2G(self, wpaPass):
        self.wait_and_set_text_element_with_delete(self.txtRepeat2G_WPAPass_xpath, wpaPass)

    def get_WPAPass_Repeat2G(self, wpaPass):
        return self.wait_and_get_attribute_element(self.txtRepeat2G_WPAPass_xpath, attribute_name='value')

    def click_Btn_Apply_Repeat2G(self):
        self.wait_and_click_element(self.btnRepeat2G_ApplySSID_xpath)

    def click_Repeat5G(self):
        self.wait_and_click_element(self.lnkRepeat5G_xpath)

    def check_Enable_Repeat5G(self):
        self.wait_and_check_checkbox(self.cbkEnableRepeat5G_xpath)

    def get_Enable_Repeat5G_status(self):
        return self.wait_and_get_checkbox_selected(self.cbkEnableRepeat5G_xpath)

    def set_SSID_Repeat5G(self, SSIDName):
        self.wait_and_set_text_element_with_delete(self.txtRepeat5G_SSID_xpath, SSIDName)

    def get_SSID_Repeat5G(self):
        return self.wait_and_get_attribute_element(self.txtRepeat5G_SSID_xpath, attribute_name='value')

    def set_BSSID_Repeat5G(self, BSSIDName):
        self.wait_and_set_text_element_with_delete(self.txtRepeat5G_BSSID_xpath, BSSIDName)

    def select_NetAuthen_Repeat5G(self, netAuthen):
        self.wait_and_select_item(self.drtRepeat5G_NetAuth_xpath, netAuthen)

    def get_NetAuthen_Repeat5G(self):
        return self.wait_and_get_selected_text(self.drtRepeat5G_NetAuth_xpath)

    def set_WPAPass_Repeat5G(self, wpaPass):
        self.wait_and_set_text_element_with_delete(self.txtRepeat5G_WPAPass_xpath, wpaPass)

    def get_WPAPass_Repeat5G(self, wpaPass):
        return self.wait_and_get_attribute_element(self.txtRepeat5G_WPAPass_xpath, attribute_name='value')

    def click_Btn_Apply_Repeat5G(self):
        self.wait_and_click_element(self.btnRepeat5G_ApplySSID_xpath)

    def naviagate_to_repeater_page(self):
        self.click_Setting_Cap()
        self.click_Wireless()
        time.sleep(1)
        self.click_Repeater()
        time.sleep(1)

    def navigate_to_repeater_2G_page(self):
        self.click_Setting_Cap()
        time.sleep(1)
        self.click_Wireless()
        time.sleep(1)
        self.click_Repeater()
        time.sleep(1)
        self.click_Repeat2G()
        time.sleep(1)

    def navigate_to_repeater_5G_page(self):
        self.click_Setting_Cap()
        time.sleep(1)
        self.click_Wireless()
        time.sleep(1)
        self.click_Repeater()
        time.sleep(1)
        self.click_Repeat5G()
        time.sleep(1)

    def setting_Repeater(self, bandW=None, enbaleCb=False, SSID=None, BSSID=None, WSecurity=None, password=None, clickApply=True):
        if bandW == '2G':
            self.click_Repeat2G()

            if enbaleCb == True:
                self.check_Enable_Repeat2G()

            if SSID is not None:
                self.set_SSID_Repeat2G(SSID)

            if WSecurity is not None:
                self.select_NetAuthen_Repeat2G(WSecurity)

            if password is not None:
                self.set_WPAPass_Repeat2G(password)

            if clickApply:
                self.click_Btn_Apply_Repeat2G()
        elif bandW == '5G':
            self.click_Repeat5G()

            if enbaleCb == True:
                self.check_Enable_Repeat5G()

            if SSID is not None:
                self.set_SSID_Repeat5G(SSID)

            if WSecurity is not None:
                self.select_NetAuthen_Repeat5G(WSecurity)

            if password is not None:
                self.set_WPAPass_Repeat5G(password)

            if clickApply:
                self.click_Btn_Apply_Repeat5G()

    def Get_Repeater_Infor(self, bandMode):
        if bandMode == '5G':
            self.click_Repeat5G()
            time.sleep(1)

            status = self.get_Enable_Repeat5G_status()

            if status == True:
                netAuth = self.get_NetAuthen_Repeat5G()
                print(netAuth)
                ssid = self.get_SSID_Repeat5G()
                if netAuth != "OPEN":
                    passW = self.get_WPAPass_Repeat5G()
                    return REPEATER_Info(
                        status=status,
                        ssidName=ssid,
                        serMode=netAuth,
                        password=passW
                    )
                else:
                    return REPEATER_Info(
                        status=status,
                        ssidName=ssid,
                        serMode=netAuth,
                        password=''
                    )
            else:
                status = self.get_Enable_Repeat5G_status()
                return REPEATER_Info(
                    status=status,
                    ssidName='',
                    serMode='',
                    password=''
                )
        elif bandMode == '2G':
            self.click_Repeat2G()
            time.sleep(1)

            status = self.get_Enable_Repeat2G_status()

            if status == True:
                netAuth = self.get_NetAuthen_Repeat2G()
                print(netAuth)
                ssid = self.get_SSID_Repeat2G()
                if netAuth != "OPEN":
                    passW = self.get_WPAPass_Repeat2G()
                    return REPEATER_Info(
                        status=status,
                        ssidName=ssid,
                        serMode=netAuth,
                        password=passW
                    )
                else:
                    return REPEATER_Info(
                        status=status,
                        ssidName=ssid,
                        serMode=netAuth,
                        password=''
                    )
            else:
                status = self.get_Enable_Repeat2G_status()
                return REPEATER_Info(
                    status=status,
                    ssidName='',
                    serMode='',
                    password=''
                )

    def get_alert_info(self):
        alert_text = self.get_alert_text()
        return (alert_text)