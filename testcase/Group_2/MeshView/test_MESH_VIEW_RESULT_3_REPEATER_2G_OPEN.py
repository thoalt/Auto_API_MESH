import random
import time
import pytest

from APIObject.login import LoginClient
from APIObject.meshAPI import meshCreateClient, meshViewClient, MESH_MODE, AUTHEN_MODE
from APIObject.openssesion import openssesionClient
from APIObject.wifi5GAPI import ssid5GViewClient

from APIObject.reset import resetClient
from base.SerialLib import Serial_Lib
from Utilities import Utility as utl
from pages.LoginPage import LoginPage
from Config import config as cfg
from pages.SettingWirelessPage import WirelessSSDIPage


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

        self.mode = MESH_MODE.REPEATER
        self.ssidName = "ThoaTest_" + str(random.randint(1, 2000))
        self.password = "1234567890_" + str(random.randint(1, 200))

        self.repeatDct = {
            "reSSID": "1111_AP_Wireless_Test_2GHz",
            "reAuthen": AUTHEN_MODE.OPEN
        }

        modeMesh = self.serialClt.Get_Mode_Mesh()
        if modeMesh != "FACTORY":
            self.serialClt.Reset_Factory()

    @pytest.mark.skip(reason="This is Manual Testcase")
    def test_MESH_CREATE_RES_1(self, driver_setup):
        try:
            ### Login After Reset Factory
            ClientSes = openssesionClient()
            cookieAfter = ClientSes.Open_Sesion_And_Get_Cookie()

            LoginClt = LoginClient()
            LoginClt.login(cookieAfter)

            # Create Mesh
            pload = self.meshCreateClt.Create_meshCreate_Pload(meshMode=self.mode,
                                                               ssidName=self.ssidName,
                                                               passW=self.password)

            pload = self.meshCreateClt.Create_meshCreate_Mode_Repeater_Pload(payload=pload,
                                                                             ReSsidName=self.repeatDct['reSSID'],
                                                                             ReAutheMode=self.repeatDct['reAuthen'])

            resBody = self.meshCreateClt.meshCreate(cookieAfter, pload=pload).body
            time.sleep(180)

            # View Mesh
            resBody = self.meshViewClt.meshView(cookieAfter).body
            self.meshViewClt.assert_meshmode(resBody, expectMode=self.mode)
            self.meshViewClt.assert_repeater(resBody, reSSIDName=self.repeatDct['reSSID'],
                                                      reAuthenMode=self.repeatDct['reAuthen'])

            time.sleep(3)

            # Tear down
            self.serialClt.Reset_Factory()
            self.serialClt.Close_Serial_Connect()
        except Exception as exc:
            print(exc)
            self.serialClt.Reset_Factory()
            self.serialClt.Close_Serial_Connect()