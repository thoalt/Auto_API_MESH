import time

import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.logout import LogoutClient
from Utilities import Utility as utl

@pytest.mark.usefixtures("create_shell")
class Test_Login():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.data = ["openSession122144124141241241241"]
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.timeLogout = 5

        SSHSes=SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        # Open Session
        self.ClientSes = openssesionClient()
        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()

        # Login
        self.LoginClt = LoginClient()
        self.LoginClt.login(self.cookie)

        # Logout
        self.LogoutClt = LogoutClient()

    def test_LOGOUT_ACT_2(self):
        time.sleep(self.timeLogout)
        resBodyLst = []
        for actionName in self.data:
            payload = self.LogoutClt.Create_Logout_Pload(action=actionName)
            resBody = self.LogoutClt.logout(cookies=self.cookie, pload=payload).body
            resBodyLst.append(resBody)
        self.LogoutClt.assert_logout_lst(resBodyLst, self.exp['code'], self.exp['msg'])


