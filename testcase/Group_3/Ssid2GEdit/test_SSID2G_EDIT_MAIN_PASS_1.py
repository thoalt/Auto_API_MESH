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
class Test_ssid2GEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success", "action": "ssid2GEdit"}
        self.ssid2GEditClt = ssid24GEditClient()
        self.ssidp = WirelessSSDIPage(self.driver)

        self.ssidIndex = 0
        self.enable = True
        self.ssid = "Test_Wifi_Main_SSID_"
        self.authenmode = "password"
        self.password = "0987654321_" + str(random.randint(1, 20000))

        self.data = [
                     "test@hec",
                    " wireless@hec",
                    "wireless@hec ",
                    "wireless@ hec",
                    "wireless@  hec",
                    "wireless@ test hec",
                    "uidwvgNleD1234567890`~!@#$%^*()_uidwvgNleD1234567890`~!@#$%^*()",
                    "uidwvgNleD1234567890-=+{[]}|;:<,uidwvgNleD1234567890-=+{[]}|;:<",
                    "uidwvgNleD1234567890.>?/txblaudpuidwvgNleD1234567890.>?/txblaud"
                     ]


    def test_ssid2GEdit_RES_1(self):
        for idx, item in enumerate(self.data):
            ranIdx = str(random.randint(1, 20000))
            pload = self.ssid2GEditClt.Create_ssid24GEdit_Pload(ssidIdx=self.ssidIndex,
                                                               enable=self.enable,
                                                               ssid=self.ssid + ranIdx,
                                                               autMode="password",
                                                               passW=item)

            resBody = self.ssid2GEditClt.ssid24GEdit(self.cookie, pload=pload).body
            time.sleep(120)

            # Get SSID in GUI
            self.ssidp.navigation_to_SSID_page()
            gui_SSID = self.ssidp.Get_SSID_Info()
            print(gui_SSID)

            # GET SSID in driver
            client = SSHClient(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH, timeout=300)
            SSHShell = client.create_shell()
            self.session = SSH_Lib(SSHShell=SSHShell)

            driver_SSID_2G = self.session.get_ssid_name(cfg.WIFI_INT_2G)
            print(driver_SSID_2G)

            with soft_assertions():
                self.ssid2GEditClt.assert_response(resBody,
                                                   self.exp['code'],
                                                   self.exp['msg'])

                # Check SSID in driver
                self.ssid2GEditClt.assert_val(self.ssid + ranIdx, driver_SSID_2G)

                if self.enable:
                    self.ssid2GEditClt.assert_val(self.ssid + ranIdx, gui_SSID.ssidName)
                    if self.authenmode != "open":
                        self.ssid2GEditClt.assert_val(item, gui_SSID.password)
