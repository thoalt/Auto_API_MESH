import random
import time
import pytest
from assertpy import soft_assertions
from sshaolin.client import SSHClient

from APIObject.wifi24GAPI import ssid24GEditClient
from pages.SettingWirelessPage import WirelessSSDIPage, WirelessGuestSSDIPage

from base.SSHLib import SSH_Lib
from Config import config as cfg

@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_ssid24GEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code":0, "msg": "Success", "action": "ssid24GEdit"}
        self.ssid24GEditClt = ssid24GEditClient()
        self.ssidp = WirelessGuestSSDIPage(self.driver)

        self.ssidIndex = 1
        self.enable = False
        self.ssid = "Test_Wifi_Guest_SSID_" + str(random.randint(1, 20000))
        self.authenmode = "open"
        self.password = "0987654321_" + str(random.randint(1, 20000))

    def test_ssid24GEdit_RES_1(self):
        pload = self.ssid24GEditClt.Create_ssid24GEdit_Pload(ssidIdx=self.ssidIndex,
                                                             enable=self.enable,
                                                             ssid=self.ssid,
                                                             autMode=self.authenmode,
                                                             passW=self.password)

        resBody = self.ssid24GEditClt.ssid24GEdit(self.cookie, pload=pload).body
        time.sleep(120)

        # Get SSID in GUI
        self.ssidp.navigation_to_Guest_SSID_setting_page()
        gui_SSID = self.ssidp.Get_GuestSSID_Infor(bandMode='2G')
        print(gui_SSID)


        with soft_assertions():
            self.ssid24GEditClt.assert_response(resBody,
                                            self.exp['code'],
                                            self.exp['msg'])

            # Check SSID in GUI
            self.ssid24GEditClt.assert_val(self.enable, gui_SSID.status)

            if self.enable:
                self.ssid24GEditClt.assert_val(self.ssid, gui_SSID.ssidName)
                if self.authenmode != "open":
                    self.ssid24GEditClt.assert_val(self.password, gui_SSID.password)

