import sys
import time
import pytest
from APIObject.wifi24GAPI import radio24GViewClient
from pages.SettingWirelessPage import WirelessRadioPage
from base.WiFiLib import Wifi_lib
from Config import config as cfg



@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_Radio2GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 0, "msg": "Success", "action": "radio2.4GView"}
        self.dataLst = ["Auto", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        self.dataExp = ["auto", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        # self.dataLst = ["1", "2"]
        # self.dataExp = ["1", "2"]

        self.radio2G = radio24GViewClient()
        self.client2G = Wifi_lib()

        self.wrp = WirelessRadioPage(self.driver)
        self.wrp.navigate_to_radio_2G_page()


    def test_RADIO_2G_CHANNEL_1(self):
        resBody_lst = []
        channel_Client_lst = []
        for data in self.dataLst:
            self.wrp.click_Btn_Edit_Radio2G()
            self.wrp.setting_Radio(bandW='2G', channel=data, clickApply=True)
            time.sleep(self.timeOut)

            # Run API Radio view
            resBody = self.radio2G.radio24GView(self.cookie).body
            resBody_lst.append(resBody)

            # Client connect to 2G CAP, then check channel
            self.client2G.forget_wifi()
            self.client2G.connect_wifi(ssid=cfg.SSID, passwd=cfg.PASSWORD, bssid=cfg.CAP_MAC_WIFI_2G)
            bssid_get = self.client2G.get_BSSID_connected(cfg.CARD_WIFI_NAME)

            if bssid_get != cfg.CAP_MAC_WIFI_2G:
                sys.exit()
            print(f"Connect to CAP via 2G Success!")

            channel_get = self.client2G.Get_Wifi_Info_Show_Interface(cfg.CARD_WIFI_NAME).channel
            channel_Client_lst.append(channel_get)

        self.radio2G.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

        self.radio2G.assert_result_lst(resBody_lst,
                                       channelLst=self.dataExp)
        print(channel_Client_lst)
        self.radio2G.assert_val_lst(self.dataExp, channel_Client_lst)
