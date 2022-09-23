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
        self.exp1 = {"code": 1, "msg": "Login Fail: Please enter correct username and password"}
        self.exp2 = {"code": 2, "msg": "You have exceeded 3 attempts in 3 minutes. Please try again in 3 minutes"}
        self.exp = {"code": 0, "msg": "Success", "action": "login", "cfg": True}
        SSHSes=SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        self.LoginClt = LoginClient()


    def test_LOGIN_STATUS_11(self):
        cookieFail = self.cookie.replace(self.cookie[:-1], self.cookie[:-2])

        # Times 1 + 2
        for i in range(0, 2):
            resBody = self.LoginClt.login(cookieFail).body
            self.LoginClt.assert_login(resBody, self.exp1['code'], self.exp1['msg'])
            time.sleep(10)

        # Times 3
        resBody = self.LoginClt.login(cookieFail).body
        self.LoginClt.assert_login(resBody, self.exp2['code'], self.exp2['msg'])

        # Times 4
        time.sleep(30)
        resBody = self.LoginClt.login(self.cookie).body
        self.LoginClt.assert_login(resBody, self.exp2['code'], self.exp2['msg'])

        # Time 5
        time.sleep(185-30)
        resBody = self.LoginClt.login(cookieFail).body
        self.LoginClt.assert_login(resBody, self.exp1['code'], self.exp1['msg'])

