import sys
import time
import pytest
from APIObject.wifi24GAPI import radio24GViewClient
from pages.SettingWirelessPage import WirelessRadioPage
from base.WiFiLib import Wifi_lib
from base.SSHLib import SSH_Lib
from Config import config as cfg


@pytest.mark.usefixtures("login", "login_CAP_GUI", "create_shell")
class Test_Radio2GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 0, "msg": "Success", "action": "radio2.4GView"}
        self.standard = "11ng"
        self.dataLst = ["20 MHz", "20/40 MHz"]
        self.dataExp = ["20MHz", "20/40MHz"]
        self.radio2G = radio24GViewClient()
        self.client2G = Wifi_lib()
        self.session = SSH_Lib(SSHShell=self.SSHShell)

        self.wrp = WirelessRadioPage(self.driver)
        self.wrp.navigate_to_radio_2G_page()


    def test_RADIO_2G_BANDWITH_1(self):
        resBody_lst = []
        bandwith_Client_lst = []
        for data in self.dataLst:
            self.wrp.click_Btn_Edit_Radio2G()
            self.wrp.setting_Radio(bandW='2G', standard=self.standard, bandwith=data, clickApply=True)
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

            # SSH then runcommand get Bitrate
            bitrate = self.session.get_bitrate(cfg.WIFI_INT_2G)

            bandW = self.client2G.Convert_Bitrate_To_Bandwith(standard=self.standard,
                                                             bitrate=bitrate)

            bandwith_Client_lst.append(bandW)

        self.radio2G.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

        self.radio2G.assert_result_lst(resBody_lst,
                                       bandWLst=self.dataExp)

        print(bandwith_Client_lst)
        self.radio2G.assert_val_lst(self.dataExp, bandwith_Client_lst)