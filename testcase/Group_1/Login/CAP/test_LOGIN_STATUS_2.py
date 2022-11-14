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
        self.exp = {"code": 0, "msg": "Success", "action": "login", "cfg": True}

        SSHSes=SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        self.LoginClt = LoginClient()

    def test_LOGIN_STATUS_2(self):
        resBody = self.LoginClt.login(self.cookie).body
        self.LoginClt.assert_login(resBody,
                                   self.exp['code'],
                                   self.exp['msg'],
                                   self.exp['action'])

        time.sleep(2)
        resBody = self.LoginClt.login(self.cookie).body
        print(resBody)
        # self.LoginClt.assert_login(resBody,
        #                            self.exp['code'],
        #                            self.exp['msg'],
        #                            self.exp['action'])