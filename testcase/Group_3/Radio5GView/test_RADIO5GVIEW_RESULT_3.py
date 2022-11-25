import sys
import time
import pytest
from APIObject.wifi5GAPI import radio5GViewClient
from pages.SettingWirelessPage import WirelessRadioPage
from base.WiFiLib import Wifi_lib
from base.SSHLib import SSH_Lib
from Config import config as cfg

@pytest.mark.usefixtures("login", "login_CAP_GUI", "create_shell")
class Test_Radio5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 0, "msg": "Success", "action": "radio5GView"}
        self.standard = '11ac'
        self.dataLst = ["20 MHz", "40 MHz", "80 MHz"]
        self.dataExp = ["20MHz", "40MHz", "80MHz"]

        self.radio5G = radio5GViewClient()
        self.client5G = Wifi_lib()
        self.session = SSH_Lib(SSHShell=self.SSHShell)

        self.wrp = WirelessRadioPage(self.driver)
        self.wrp.navigate_to_radio_5G_page()

    def test_RADIO_5G_BANDWIDTH_1(self):
        resBody_lst = []
        bandwith_Client_lst = []

        for data in self.dataLst:
            self.wrp.click_Btn_Edit_Radio5G()

            self.wrp.setting_Radio(bandW='5G', standard=self.standard, bandwith=data, clickApply=True)
            time.sleep(self.timeOut)

            # Click to tab Radio 5G again
            self.wrp.click_Radio5G()

            #Call API Radio view
            resBody = self.radio5G.radio5GView(self.cookie).body
            resBody_lst.append(resBody)

            # # SSH then check the bitrate. From Bitrate convert to bandwith
            # self.client5G.forget_wifi()
            # self.client5G.connect_wifi(ssid=cfg.SSID, passwd=cfg.PASSWORD, bssid=cfg.CAP_MAC_WIFI_5G)
            # bssid_get = self.client5G.get_BSSID_connected(cfg.CARD_WIFI_NAME)
            #
            # if bssid_get != cfg.CAP_MAC_WIFI_5G:
            #     sys.exit()
            #
            # # SSH then run command get Bitrate
            # bitrate = self.session.get_bitrate(cfg.WIFI_INT_5G)
            # bandW = self.client5G.Convert_Bitrate_To_Bandwith(standard=self.standard,
            #                                                bitrate=bitrate)
            # bandwith_Client_lst.append(bandW)

        self.radio5G.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

        self.radio5G.assert_result_lst(resBody_lst,
                                       bandWLst=self.dataExp)
        # print(bandwith_Client_lst)
        # self.radio5G.assert_val_lst(self.dataExp, bandwith_Client_lst)