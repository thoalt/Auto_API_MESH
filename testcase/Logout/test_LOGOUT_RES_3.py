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
        self.data = []
        self.exp = {"code": 15, "msg": "Session Timeout"}
        self.timeLogout = 610

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


    def test_LOGOUT_RES_3(self):
        time.sleep(self.timeLogout)
        resBody = self.LogoutClt.logout(cookies=self.cookie).body
        self.LogoutClt.assert_logout(resBody,
                                   self.exp['code'],
                                   self.exp['msg'])

