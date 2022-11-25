import sys
import time
import pytest
from APIObject.wifi5GAPI import radio5GViewClient
from pages.SettingWirelessPage import WirelessRadioPage
from base.WiFiLib import Wifi_lib
from Config import config as cfg

@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_Radio5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 0, "msg": "Success", "action": "radio5GView"}
        self.dataLst = ["Auto", "36", "40", "44", "48", "52", "56", "60", "64", "100", "104", "112", "116", "120", "124", "128", "132", "136", "140", "144", "149", "153", "157", "161", "165"]
        self.dataExp = ["auto", "36", "40", "44", "48", "52", "56", "60", "64", "100", "104", "112", "116", "120", "124", "128", "132", "136", "140", "144", "149", "153", "157", "161", "165"]

        # self.dataLst = ["36", "40"]
        # self.dataExp = ["36", "40"]

        self.radio5G = radio5GViewClient()
        self.client5G = Wifi_lib()

        self.wrp = WirelessRadioPage(self.driver)


    def test_RADIO_5G_CHANNEL_1(self):
        resBody_lst = []
        channel_Client_lst = []
        for data in self.dataLst:
            self.wrp.navigate_to_radio_5G_page()
            self.wrp.click_Btn_Edit_Radio5G()

            self.wrp.setting_Radio(bandW='5G', standard='11ac', channel=data, clickApply=True)
            time.sleep(self.timeOut)

            # Click to tab Radio 5G again
            # self.wrp.click_Radio5G()

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
            # channel_get = self.client5G.Get_Wifi_Info_Show_Interface(cfg.CARD_WIFI_NAME).channel
            # channel_Client_lst.append(channel_get)

        self.radio5G.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

        self.radio5G.assert_result_lst(resBody_lst,
                                       channelLst=self.dataExp)
        # print(channel_Client_lst)
        # self.radio5G.assert_val_lst(self.dataExp, channel_Client_lst)