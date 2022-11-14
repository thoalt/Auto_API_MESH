import random
import time
import pytest
from assertpy import soft_assertions
from sshaolin.client import SSHClient

from APIObject.wifi5GAPI import ssid5GEditClient
from base.WiFiLib import Wifi_lib
from pages.SettingWirelessPage import WirelessSSDIPage, WirelessGuestSSDIPage

from base.SSHLib import SSH_Lib
from Config import config as cfg


@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_ssid5GEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success", "action": "ssid5GEdit"}
        self.ssid5GEditClt = ssid5GEditClient()
        self.ssidp = WirelessSSDIPage(self.driver)

        self.ssidIndex = 0
        self.enable = True
        self.ssid = "Test_Wifi_Main_SSID_" + str(random.randint(1, 20000))
        self.authenmode = "password"
        self.password = "0987654321_"

        self.data = ["e", "5", "%", "`", "t!", "gh", "3#",
                     "test@hec", " wireless@hec", "wireless@hec ", "wireless@ hec", "wireless@  hec",
                     "wireless@ test hec",
                     "uidwvgNleD1234567890`~!@#$%^*()_",
                     "uidwvgNleD1234567890-=+{[]}|;:<",
                     "uidwvgNleD1234567890.>?/txblaudp"]

    def test_ssid5GEdit_RES_1(self):
        for idx, item in enumerate(self.data):
            ranIdx = str(random.randint(1, 20000))
            pload = self.ssid5GEditClt.Create_ssid5GEdit_Pload(ssidIdx=self.ssidIndex,
                                                               enable=self.enable,
                                                               ssid=item,
                                                               autMode=self.authenmode,
                                                               passW=self.password + ranIdx)

            resBody = self.ssid5GEditClt.ssid5GEdit(self.cookie, pload=pload).body
            time.sleep(120)

            # Get SSID in GUI
            self.ssidp.navigation_to_SSID_page()
            gui_SSID = self.ssidp.Get_SSID_Info()
            print(gui_SSID)

            # GET SSID in driver
            client = SSHClient(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH, timeout=300)
            SSHShell = client.create_shell()
            self.session = SSH_Lib(SSHShell=SSHShell)

            driver_SSID_5G = self.session.get_ssid_name(cfg.WIFI_INT_5G)
            print(driver_SSID_5G)

            with soft_assertions():
                self.ssid5GEditClt.assert_response(resBody,
                                                   self.exp['code'],
                                                   self.exp['msg'])

                # Check SSID in driver
                self.ssid5GEditClt.assert_val(item, driver_SSID_5G)

                if self.enable:
                    self.ssid5GEditClt.assert_val(item, gui_SSID.ssidName)
                    if gui_SSID.serMode != "OPEN":
                        self.ssid5GEditClt.assert_val(self.password + ranIdx, gui_SSID.password)
