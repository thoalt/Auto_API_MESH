import time

import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from Utilities import Utility as utl
from base.SerialLib import Serial_Lib
from pages.MeshPage import MeshPage
import Config.config as cfg
@pytest.mark.usefixtures("login_CAP_GUI")
class Test_Login():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.data = []
        self.exp = {"code": 0, "msg": "Success", "action": "login", "cfg": True}

        self.serialClt = Serial_Lib()
        self.mp = MeshPage(self.driver)

        # Create Mesh Before Login
        modeMesh = self.serialClt.Get_Mode_Mesh()
        if modeMesh == "FACTORY":
            self.mp.navigate_to_create_mesh_network()
            self.mp.set_create_mesh(SSID=cfg.SSID, password=cfg.PASSWORD, clickAction=True)
            time.sleep(180)

        self.ClientSes = openssesionClient()
        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()

        print("***************** COOKIE **************")
        print(self.cookie)
        self.LoginClt = LoginClient()


    def test_LOGIN_SES_1(self):
        resBody = self.LoginClt.login(self.cookie).body
        self.LoginClt.assert_login(resBody,
                                   self.exp['code'],
                                   self.exp['msg'],
                                   self.exp['action'],
                                   self.exp['cfg'])
