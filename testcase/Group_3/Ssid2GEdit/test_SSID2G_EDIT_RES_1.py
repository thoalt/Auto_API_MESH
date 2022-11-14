import time
import pytest
from APIObject.wifi24GAPI import ssid24GEditClient
from pages.SettingWirelessPage import WirelessSSDIPage

from base.SSHLib import SSH_Lib
from Config import config as cfg

@pytest.mark.usefixtures("login", "login_CAP_GUI", "create_shell")
class Test_ssid2GEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code":0 , "msg": "Success", "action": "ssid2GEdit"}
        self.ssid2GEditClt = ssid24GEditClient()
        self.session = SSH_Lib(SSHShell=self.SSHShell)
        self.ssidp = WirelessSSDIPage(self.driver)

        self.ssidIndex = 0
        self.enable = True
        self.ssid = "Test_Wifi"
        self.authenmode = "password"
        self.password = "1234567890"

    def test_ssid2GEdit_RES_1(self):
        time.sleep(self.timeOut)
        pload = self.ssid2GEditClt.Create_ssid24GEdit_Pload(ssidIdx=self.ssidIndex,
                                                             enable=self.enable,
                                                             ssid = self.ssid,
                                                             autMode=self.authenmode,
                                                             passW=self.password)

        resBody = self.ssid2GEditClt.ssid24GEdit(self.cookie, pload=pload).body
        self.ssid2GEditClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
        time.sleep(120)

        # Check SSID in driver
        driver_SSID = self.session.get_ssid_name(cfg.WIFI_INT_2G)
        self.ssid2GEditClt.assert_val(self.ssid, driver_SSID)

        # Check SSID in GUI
        self.ssidp.navigation_to_SSID_page()
        gui_SSID = self.ssidp.Get_SSID_Info()
        self.ssid2GEditClt.assert_val(self.ssid, gui_SSID.ssidName)
        self.ssid2GEditClt.assert_val(self.password, gui_SSID.password)

