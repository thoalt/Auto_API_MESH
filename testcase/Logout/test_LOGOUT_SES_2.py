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
        self.exp = {"code": 12, "msg": "Unknown Error"}

        SSHSes=SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        # Open Session
        self.ClientSes = openssesionClient()
        self.sesID, self.salt, self.reqID = self.ClientSes.Open_Session_And_Get_Session_ID()

        self.md5 = self.ClientSes.Calculate_md5(sessionID=self.sesID, salt=self.salt)
        self.cookie = self.ClientSes.Create_Cookie(sessionID=self.sesID, md5=self.md5)

        # Login
        self.LoginClt = LoginClient()
        self.LoginClt.login(self.cookie)

        # Logout
        self.LogoutClt = LogoutClient()
        time.sleep(10)

        self.data = [self.sesID[:-1], self.sesID[0:5], "a012afeb"]

    def test_LOGOUT_SES_2(self):
        resBodyLst = []
        for item in self.data:
            cookie = self.ClientSes.Create_Cookie(sessionID=item, md5=self.md5)
            resBody = self.LogoutClt.logout(cookies=cookie).body
            resBodyLst.append(resBody)
        self.LoginClt.assert_login_list(resBodyLst,
                                        self.exp['code'],
                                        self.exp['msg'])
