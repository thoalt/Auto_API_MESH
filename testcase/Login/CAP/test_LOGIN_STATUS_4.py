import time

import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from Utilities import Utility as utl

@pytest.mark.usefixtures("create_shell")
class Test_Login():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.data = []
        self.expF = {"code": 1, "msg": "Login Fail: Please enter correct username and password"}
        self.exp = {"code": 0, "msg": "Success", "action": "login", "cfg": True}
        SSHSes=SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        self.LoginClt = LoginClient()


    def test_LOGIN_STATUS_4(self):
        cookieFail = self.cookie.replace(self.cookie[:-1], self.cookie[:-2])

        # Times 1 + 2
        for i in range(0, 2):
            resBody = self.LoginClt.login(cookieFail).body
            self.LoginClt.assert_login(resBody, self.expF['code'], self.expF['msg'])
            time.sleep(10)
