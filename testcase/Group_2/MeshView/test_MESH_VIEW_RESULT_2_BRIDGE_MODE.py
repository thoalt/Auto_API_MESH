import random
import time

import assertpy
import pytest

from APIObject.login import LoginClient
from APIObject.meshAPI import meshCreateClient, meshViewClient, MESH_MODE, AUTHEN_MODE
from APIObject.openssesion import openssesionClient
from APIObject.wifi5GAPI import ssid5GViewClient
from APIObject.reset import resetClient
from base.SerialLib import Serial_Lib
from pages.LoginPage import LoginPage
from pages.SettingWANPage import SettingWANPage
import Config.config as cfg
from Utilities import Utility as utl
from base.WiFiLib import Wifi_lib
from pages.SettingWirelessPage import WirelessSSDIPage


@pytest.mark.usefixtures("login_without_create_mesh")
class Test_Mesh_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success"}
        self.clientSes = openssesionClient()
        self.meshCreateClt = meshCreateClient()
        self.meshViewClt = meshViewClient()
        self.ssidViewClt = ssid5GViewClient()
        self.resetClt = resetClient()
        self.wifiClt = Wifi_lib()
        self.serialClt = Serial_Lib()

        self.mode = MESH_MODE.BRIDGE
        self.ssidName = "ThoaTest_" + str(random.randint(1, 2000))
        self.password = "1234567890_" + str(random.randint(1, 200))
        self.loopAvoid = True

        modeMesh = self.serialClt.Get_Mode_Mesh()
        if modeMesh != "FACTORY":
            self.serialClt.Reset_Factory()

    @pytest.mark.skip(reason="This is Manual Testcase")
    def test_MESH_CREATE_RES_1(self, driver_setup):
        try:
            ## Login After Reset Factory
            cookieAfter = self.clientSes.Open_Sesion_And_Get_Cookie()
            LoginClt = LoginClient()
            LoginClt.login(cookieAfter)

            # Create Mesh
            pload = self.meshCreateClt.Create_meshCreate_Pload(meshMode=self.mode,
                                                               ssidName=self.ssidName,
                                                               passW=self.password)

            pload = self.meshCreateClt.Create_meshCreate_Mode_Brigde_Pload(payload=pload,
                                                                           loopAvoid=self.loopAvoid)

            resBody = self.meshCreateClt.meshCreate(cookieAfter, pload=pload).body
            time.sleep(180)

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

            # Tear down
            self.serialClt.Reset_Factory()
            self.serialClt.Close_Serial_Connect()
        except Exception as exc:
            print(exc)
            self.serialClt.Reset_Factory()
            self.serialClt.Close_Serial_Connect()