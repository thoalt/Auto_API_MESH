import random
import time
import pytest
from assertpy import soft_assertions
from sshaolin.client import SSHClient

from APIObject.wifi5GAPI import ssid5GEditClient
from pages.SettingWirelessPage import WirelessSSDIPage, WirelessGuestSSDIPage

from base.SSHLib import SSH_Lib
from Config import config as cfg

@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_ssid5GEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code":0, "msg": "Success", "action": "ssid5GEdit"}
        self.ssid5GEditClt = ssid5GEditClient()
        self.ssidp = WirelessGuestSSDIPage(self.driver)

        self.ssidIndex = 1
        self.enable = True
        self.ssid = "Test_Wifi_Guest_SSID_" + str(random.randint(1, 20000))
        self.authenmode = "password"
        self.password = "0987654321_" + str(random.randint(1, 20000))

    def test_ssid5GEdit_RES_1(self):
        pload = self.ssid5GEditClt.Create_ssid5GEdit_Pload(ssidIdx=self.ssidIndex,
                                                             enable=self.enable,
                                                             ssid=self.ssid,
                                                             autMode=self.authenmode,
                                                             passW=self.password)

        resBody = self.ssid5GEditClt.ssid5GEdit(self.cookie, pload=pload).body
        time.sleep(120)

        # Get SSID in GUI
        self.ssidp.navigation_to_Guest_SSID_setting_page()
        gui_SSID = self.ssidp.Get_GuestSSID_Infor(bandMode='5G')
        print(gui_SSID)

        # GET SSID in driver
        client = SSHClient(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH, timeout=300)
        SSHShell = client.create_shell()
        self.session = SSH_Lib(SSHShell=SSHShell)

        driver_SSID_5G = self.session.get_ssid_name(cfg.WIFI_GUEST_INT_5G)
        print(driver_SSID_5G)

        with soft_assertions():
            self.ssid5GEditClt.assert_response(resBody,
                                            self.exp['code'],
                                            self.exp['msg'])

            # Check SSID in driver
            self.ssid5GEditClt.assert_val(self.ssid, driver_SSID_5G)

            # Check SSID in GUI
            self.ssid5GEditClt.assert_val(self.enable, gui_SSID.status)

            if self.enable:
                self.ssid5GEditClt.assert_val(self.ssid, gui_SSID.ssidName)
                if self.authenmode != "open":
                    self.ssid5GEditClt.assert_val(self.password, gui_SSID.password)
