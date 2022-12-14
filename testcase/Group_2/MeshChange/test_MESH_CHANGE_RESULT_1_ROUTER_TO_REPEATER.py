import random
import time
import pytest

from APIObject.login import LoginClient
from APIObject.meshAPI import meshCreateClient, meshViewClient, MESH_MODE, AUTHEN_MODE, meshChangeClient
from APIObject.openssesion import openssesionClient
from APIObject.wifi5GAPI import ssid5GViewClient

from APIObject.reset import resetClient
from base.SerialLib import Serial_Lib
from base.WiFiLib import Wifi_lib
from pages.LoginPage import LoginPage
from pages.SettingWirelessPage import WirelessSSDIPage
from Config import config as cfg
from Utilities import Utility as utl
#
# @pytest.mark.usefixtures("login_without_create_mesh")
class Test_Mesh_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success"}
        self.meshCreateClt = meshCreateClient()
        self.meshViewClt = meshViewClient()
        self.meshChangeClt = meshChangeClient()
        self.ssidViewClt = ssid5GViewClient()
        self.resetClt = resetClient()
        self.serialClt = Serial_Lib()
        self.wifiClt = Wifi_lib()

        self.mode = MESH_MODE.REPEATER
        self.ssidName = "ThoaTest_" + str(random.randint(1, 2000))
        self.password = "1234567890_" + str(random.randint(1, 200))
        self.loopAvoid = True
        self.repeatDct = {
            "reSSID": "1111_AP_Wireless_Test_2GHz",
            "reAuthen": AUTHEN_MODE.OPEN
        }

        modeMesh = self.serialClt.Get_Mode_Mesh()
        if modeMesh != "FACTORY":
            self.serialClt.Reset_Factory()

        # Create Mesh
        ClientSes = openssesionClient()
        LoginClt = LoginClient()

        self.cookie = ClientSes.Open_Sesion_And_Get_Cookie()

        pload = self.meshCreateClt.Create_meshCreate_Pload(meshMode=MESH_MODE.ROUTER,
                                                           ssidName="ThoaTest_RouterMode",
                                                           passW="1234567890")

        resBody = self.meshCreateClt.meshCreate(self.cookie, pload=pload).body
        time.sleep(120)


    @pytest.mark.skip(reason="This is Manual Testcase")
    def test_MESH_CREATE_RES_1(self, driver_setup):
        try:
            ### Login After Reset Factory

            # Change Mesh
            pload = self.meshChangeClt.Create_meshChange_Pload(meshMode=self.mode,
                                                               ssidName=self.ssidName,
                                                               passW=self.password)
            pload = self.meshChangeClt.Create_meshChange_Mode_Repeater_Pload(payload=pload,
                                                                             ReSsidName=self.repeatDct['reSSID'],
                                                                             ReAutheMode=self.repeatDct['reAuthen'])

            resBody = self.meshChangeClt.meshChange(self.cookie, pload=pload).body
            time.sleep(120)

            # View Mesh
            resBody = self.meshViewClt.meshView(cookieAfter).body
            self.meshViewClt.assert_meshmode(resBody, expectMode=self.mode)
            self.meshViewClt.assert_repeater(resBody, reSSIDName=self.repeatDct['reSSID'],
                                             reAuthenMode=self.repeatDct['reAuthen'])

            time.sleep(3)
            # View SSID
            resBody = self.ssidViewClt.ssid5GView(cookieAfter).body
            self.ssidViewClt.assert_ssid5GView_result(resBody, ssidName=self.ssidName, passWord=self.password)

            # Login to Webgui
            driver = driver_setup
            lp = LoginPage(driver)
            lp.open_url(cfg.CAP_URL)
            lp.log_in_to_webgui(cfg.USER_GUI, cfg.PASS_GUI)

            # View SSID Page
            ssidp = WirelessSSDIPage(driver)
            ssidp.navigation_to_SSID_page()
            gui_SSID = self.ssidp.Get_SSID_Info()
            driver.close()

            self.meshCreateClt.assert_val(self.ssidName, gui_SSID.ssidName)
            self.meshCreateClt.assert_val("WPA2-PSK", gui_SSID.serMode)
            self.meshCreateClt.assert_val(self.password, gui_SSID.password)

            # Tear down
            self.serialClt.Reset_Factory()
            self.serialClt.Close_Serial_Connect()
        except Exception as exc:
            print(exc)
            self.serialClt.Reset_Factory()
            self.serialClt.Close_Serial_Connect()