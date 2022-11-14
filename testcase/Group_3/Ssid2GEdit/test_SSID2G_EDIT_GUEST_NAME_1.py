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
        self.exp = {"code": 0, "msg": "Success", "action": "ssid24GEdit"}
        self.ssid24GEditClt = ssid24GEditClient()
        self.ssidp = WirelessGuestSSDIPage(self.driver)

        self.ssidIndex = 1
        self.enable = True
        self.ssid = "Test_Wifi_Guest_SSID_" + str(random.randint(1, 20000))
        self.authenmode = "password"
        self.password = "0987654321_"

        self.data = ["e", "5", "%", "`", "t!", "gh", "3#",
                     "test@hec", " wireless@hec", "wireless@hec ", "wireless@ hec", "wireless@  hec",
                     "wireless@ test hec",
                     "uidwvgNleD1234567890`~!@#$%^*()_",
                     "uidwvgNleD1234567890-=+{[]}|;:<",
                     "uidwvgNleD1234567890.>?/txblaudp"]

    def test_ssid24GEdit_RES_1(self):
        ranIdx = str(random.randint(1, 20000))
        for idx, item in enumerate(self.data):
            if idx % 2 == 0:
                pload = self.ssid24GEditClt.Create_ssid24GEdit_Pload(ssidIdx=self.ssidIndex,
                                                                     enable=self.enable,
                                                                     ssid=item,
                                                                     autMode="password",
                                                                     passW=self.password + ranIdx)
            else:
                pload = self.ssid24GEditClt.Create_ssid24GEdit_Pload(ssidIdx=self.ssidIndex,
                                                                     enable=self.enable,
                                                                     ssid=item,
                                                                     autMode="open",
                                                                     passW=self.password + ranIdx)

            resBody = self.ssid24GEditClt.ssid24GEdit(self.cookie, pload=pload).body
            time.sleep(120)

            # Get SSID in GUI
            self.ssidp.navigation_to_Guest_SSID_setting_page()
            gui_SSID = self.ssidp.Get_GuestSSID_Infor(bandMode='2G')
            print(gui_SSID)

            # GET SSID in driver
            client = SSHClient(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH, timeout=300)
            SSHShell = client.create_shell()
            self.session = SSH_Lib(SSHShell=SSHShell)

            driver_SSID_24G = self.session.get_ssid_name(cfg.WIFI_GUEST_INT_2G)
            print(driver_SSID_24G)

            with soft_assertions():
                self.ssid24GEditClt.assert_response(resBody,
                                                    self.exp['code'],
                                                    self.exp['msg'])

                # Check SSID in driver
                self.ssid24GEditClt.assert_val(item, driver_SSID_24G, desc="SSID IN DRIVER")

                # Check SSID in GUI
                self.ssid24GEditClt.assert_val(self.enable, gui_SSID.status, desc="STATUS IN GUI")

                if self.enable:
                    self.ssid24GEditClt.assert_val(item, gui_SSID.ssidName, desc="SSID NAME IN GUI")
                    if gui_SSID.serMode != "OPEN":
                        self.ssid24GEditClt.assert_val(self.password + ranIdx, gui_SSID.password, desc="PASS IN GUI")
