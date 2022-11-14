import random
import time
import pytest
from assertpy import soft_assertions
from sshaolin.client import SSHClient

from APIObject.wifi5GAPI import ssid5GEditClient
from pages.SettingWirelessPage import WirelessSSDIPage

from base.SSHLib import SSH_Lib
from Config import config as cfg

@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_ssid5GEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code":11 , "msg": "Verify Fail", "action": "ssid5GEdit"}
        self.ssid5GEditClt = ssid5GEditClient()
        self.ssidp = WirelessSSDIPage(self.driver)

        self.ssidIndex = 0
        self.enable = False
        self.ssid = "Test_Wifi_" + str(random.randint(1, 20000))
        self.authenmode = "password"
        self.password = "1234567890_" + str(random.randint(1, 20000))

    def test_ssid5GEdit_RES_1(self):
        """
        Main SSID always Enable and in Password Mode
        """
        time.sleep(self.timeOut)
        pload = self.ssid5GEditClt.Create_ssid5GEdit_Pload(ssidIdx=self.ssidIndex,
                                                             enable=self.enable,
                                                             ssid=self.ssid,
                                                             autMode=self.authenmode,
                                                             passW=self.password)

        resBody = self.ssid5GEditClt.ssid5GEdit(self.cookie, pload=pload).body
        time.sleep(5)
        with soft_assertions():
            self.ssid5GEditClt.assert_response(resBody,
                                            self.exp['code'],
                                            self.exp['msg'])
