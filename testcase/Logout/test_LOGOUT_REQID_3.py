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
        self.data = [-1]
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.timeLogout = 5

        SSHSes=SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()


    def test_LOGOUT_REQID_2(self):
        time.sleep(self.timeLogout)
        resBodyLst = []
        for reqID in self.data:
            # Open Session
            self.ClientSes = openssesionClient()
            self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()

            # Login
            self.LoginClt = LoginClient()
            self.LoginClt.login(self.cookie)

            # Logout
            self.LogoutClt = LogoutClient()

            payload = self.LogoutClt.Create_Logout_Pload(reqID=reqID)
            resBody = self.LogoutClt.logout(cookies=self.cookie, pload=payload).body
            resBodyLst.append(resBody)
            time.sleep(2)
        self.LogoutClt.assert_logout_lst(resBodyLst, self.exp['code'], self.exp['msg'])
