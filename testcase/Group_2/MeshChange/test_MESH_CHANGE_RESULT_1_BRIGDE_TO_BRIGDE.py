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
from pages.SettingWANPage import SettingWANPage
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

        self.mode = MESH_MODE.BRIDGE
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

        pload = self.meshCreateClt.Create_meshCreate_Pload(meshMode=MESH_MODE.BRIDGE,
                                                           ssidName="ThoaTest_BridgeMode",
                                                           passW="1234567890")
        pload = self.meshChangeClt.Create_meshChange_Mode_Brigde_Pload(payload=pload,
                                                                       loopAvoid=self.loopAvoid)

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
            pload = self.meshChangeClt.Create_meshChange_Mode_Brigde_Pload(payload=pload,
                                                                            loopAvoid=self.loopAvoid )

            resBody = self.meshChangeClt.meshChange(self.cookie, pload=pload).body
            time.sleep(120)

            ## If Bridge Mode --> Login Again
            ipAddr = self.serialClt.Get_IP_Address()
            print("\n IPADDR: " + str(ipAddr))
            url_gui = f"http://{ipAddr}/"
            url_Login = f"https://{ipAddr}:9000/onelinklogin"
            url_Agent = f"https://{ipAddr}:9000/onelinkagent"
            print(url_Login)

            self.wifiClt.connect_wifi(ssid=self.ssidName, passwd=self.password, bssid=cfg.CAP_MAC_WIFI_5G)
            # self.wifiClt.connect_wifi(ssid="ThoaTest_534", passwd="1234567890_107", bssid=cfg.CAP_MAC_WIFI_5G)

            ClientSes = openssesionClient(url=url_Login)
            cookieAfter = ClientSes.Open_Sesion_And_Get_Cookie()

            LoginClt = LoginClient(url=url_Login)
            LoginClt.login(cookieAfter)

            MeshViewClt = meshViewClient(url=url_Agent)
            # View Mesh
            resBody = MeshViewClt.meshView(cookieAfter).body
            MeshViewClt.assert_meshmode(resBody, expectMode=self.mode, loopAvoid=str(self.loopAvoid))

            SsidViewClt = ssid5GViewClient(url=url_Agent)
            # View SSID
            resBody = SsidViewClt.ssid5GView(cookieAfter).body
            SsidViewClt.assert_ssid5GView_result(resBody, ssidName=self.ssidName, passWord=self.password)
            # SsidViewClt.assert_ssid5GView_result(resBody, ssidName="ThoaTest_534", passWord="1234567890_107")

            # Login to Webgui
            driver = driver_setup
            lp = LoginPage(driver)
            lp.open_url(url_gui)
            lp.log_in_to_webgui(cfg.USER_GUI, cfg.PASS_GUI)

            # View WanPage in mode Bridge
            wanP = SettingWANPage(driver)
            wanP.navigate_to_WAN_page()
            wanType = wanP.get_wantype_overpage()
            self.meshCreateClt.assert_val(wanType, "Wan Bridge")

            # View SSID Page
            ssidp = WirelessSSDIPage(self.driver)
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