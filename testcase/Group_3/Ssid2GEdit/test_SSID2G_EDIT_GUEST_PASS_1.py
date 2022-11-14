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
        self.ssid = "Test_Wifi_GUEST_SSID_"
        self.authenmode = "password"
        self.password = "0987654321_" + str(random.randint(1, 20000))

        self.data = ["test@hec",
                    " wireless@hec",
                    "wireless@hec ",
                    "wireless@ hec",
                    "wireless@  hec",
                    "wireless@ test hec",
                    "uidwvgNleD1234567890`~!@#$%^*()_uidwvgNleD1234567890`~!@#$%^*()",
                    "uidwvgNleD1234567890-=+{[]}|;:<,uidwvgNleD1234567890-=+{[]}|;:<",
                    "uidwvgNleD1234567890.>?/txblaudpuidwvgNleD1234567890.>?/txblaud"
                     ]

    def test_ssid24GEdit_RES_1(self):

        for idx, item in enumerate(self.data):
            ranIdx = str(random.randint(1, 20000))
            pload = self.ssid24GEditClt.Create_ssid24GEdit_Pload(ssidIdx=self.ssidIndex,
                                                               enable=self.enable,
                                                               ssid=self.ssid + ranIdx,
                                                               autMode="password",
                                                               passW=item)

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


                # Check SSID in GUI
                self.ssid24GEditClt.assert_val(self.enable, gui_SSID.status)

                if self.enable:
                    self.ssid24GEditClt.assert_val(self.ssid + ranIdx, gui_SSID.ssidName)
                    if gui_SSID.serMode != "OPEN":
                        self.ssid24GEditClt.assert_val(item, gui_SSID.password)
