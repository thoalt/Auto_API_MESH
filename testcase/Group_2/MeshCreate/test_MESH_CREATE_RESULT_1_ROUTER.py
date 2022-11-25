import random
import time
import pytest

from APIObject.login import LoginClient
from APIObject.meshAPI import meshCreateClient, meshViewClient, MESH_MODE, AUTHEN_MODE
from APIObject.openssesion import openssesionClient
from APIObject.wifi5GAPI import ssid5GViewClient

from APIObject.reset import resetClient
from APIObject.topology import topologyClient
from base.SerialLib import Serial_Lib
from base.WiFiLib import Wifi_lib
from pages.LoginPage import LoginPage
from pages.SettingWirelessPage import WirelessSSDIPage
from Config import config as cfg
from Utilities import Utility as utl

@pytest.mark.usefixtures("login_without_create_mesh")
class Test_Mesh_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success"}
        self.meshCreateClt = meshCreateClient()
        self.meshViewClt = meshViewClient()
        self.ssidViewClt = ssid5GViewClient()
        self.resetClt = resetClient()
        self.serialClt = Serial_Lib()
        self.wifiClt = Wifi_lib()
        self.topoClt = topologyClient()

        self.mode = MESH_MODE.ROUTER
        self.ssidName = "ThoaTest_" + str(random.randint(1, 2000))
        self.password = "1234567890_" + str(random.randint(1, 200))
        self.addNode = True

        modeMesh = self.serialClt.Get_Mode_Mesh()
        if modeMesh != "FACTORY":
            self.serialClt.Reset_Factory()

    # @pytest.mark.skip(reason="This is Manual Testcase")
    def test_MESH_CREATE_RES_1(self, driver_setup):
        try:
            ### Login After Reset Factory
            ClientSes = openssesionClient()
            LoginClt = LoginClient()

            cookieAfter = ClientSes.Open_Sesion_And_Get_Cookie()
            LoginClt.login(cookieAfter)

            # Create Mesh
            pload = self.meshCreateClt.Create_meshCreate_Pload(meshMode=self.mode,
                                                               ssidName=self.ssidName,
                                                               passW=self.password,
                                                               addNode=self.addNode)

            resBody = self.meshCreateClt.meshCreate(cookieAfter, pload=pload).body
            time.sleep(120)

            # View Mesh
            resBody = self.meshViewClt.meshView(cookieAfter).body
            self.meshViewClt.assert_meshmode(resBody, expectMode=self.mode)

            # View SSID
            resBody = self.ssidViewClt.ssid5GView(cookieAfter).body
            self.ssidViewClt.assert_ssid5GView_result(resBody, ssidName=self.ssidName, passWord=self.password)

            time.sleep(3)
            # Topology
            resBody_topo = self.topoClt.topology(cookies=cookieAfter).body

            # Login to Webgui
            driver = driver_setup
            lp = LoginPage(driver)
            lp.open_url(cfg.CAP_URL)
            lp.log_in_to_webgui(cfg.USER_GUI, cfg.PASS_GUI)

            # View SSID Page
            ssidp = WirelessSSDIPage(driver)
            ssidp.navigation_to_SSID_page()
            gui_SSID = ssidp.Get_SSID_Info()
            driver.close()

            self.meshCreateClt.assert_val(self.ssidName, gui_SSID.ssidName)
            self.meshCreateClt.assert_val("WPA2-PSK", gui_SSID.serMode)
            self.meshCreateClt.assert_val(self.password, gui_SSID.password)

            # Tear down
            # self.serialClt.Reset_Factory()
            # self.serialClt.Close_Serial_Connect()
        except Exception as exc:
            print(exc)
            self.serialClt.Reset_Factory()
            self.serialClt.Close_Serial_Connect()
            assert False