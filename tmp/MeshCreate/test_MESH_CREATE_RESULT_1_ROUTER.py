import random
import time
import pytest

from APIObject.login import LoginClient
from APIObject.meshAPI import meshCreateClient, meshViewClient, MESH_MODE, AUTHEN_MODE
from APIObject.openssesion import openssesionClient
from APIObject.wifi5GAPI import ssid5GViewClient

from APIObject.reset import resetClient
from Utilities import Utility as utl

@pytest.mark.usefixtures("login")
class Test_Mesh_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success"}
        self.meshCreateClt = meshCreateClient()
        self.meshViewClt = meshViewClient()
        self.ssidViewClt = ssid5GViewClient()

        self.mode = MESH_MODE.ROUTER
        self.ssidName = "ThoaTest_" + str(random.randint(1, 2000))
        self.password = "1234567890_" + str(random.randint(1, 200))

        self.resetClt = resetClient()
        self.resetClt.reset_CAP(self.cookie)

    #@pytest.mark.skip(reason="This is Manual Testcase")
    def test_WAN_CREATE_RES_1(self):
        time.sleep(240)
        ### Login After Reset Factory
        ClientSes = openssesionClient()
        cookieAfter = ClientSes.Open_Sesion_And_Get_Cookie()

        LoginClt = LoginClient()
        LoginClt.login(cookieAfter)

        # Create Mesh
        pload = self.meshCreateClt.Create_meshCreate_Pload(meshMode=self.mode,
                                                           ssidName=self.ssidName,
                                                           passW=self.password)

        resBody = self.meshCreateClt.meshCreate(cookieAfter, pload=pload).body
        time.sleep(120)

        # View Mesh
        resBody = self.meshViewClt.meshView(cookieAfter).body
        self.meshViewClt.assert_meshmode(resBody, expectMode=self.mode)

        # View SSID
        resBody = self.ssidViewClt.ssid5GView(self.cookie).body
        self.ssidViewClt.assert_ssid5GView_result(resBody, ssidName=self.ssidName, passWord=self.password)
