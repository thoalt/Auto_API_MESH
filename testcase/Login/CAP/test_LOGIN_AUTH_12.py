import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from Utilities import Utility as utl
from Config import config as cfg

@pytest.mark.usefixtures("create_shell")
class Test_Login():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):

        self.exp = {"code": 1, "msg": "Login Fail: Please enter correct username and password"}

        SSHSes=SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.sesID, self.salt, self.reqID = self.ClientSes.Open_Session_And_Get_Session_ID()

        self.md5 = self.ClientSes.Calculate_md5(sessionID=self.sesID, salt=self.salt)
        self.cookie = self.ClientSes.Create_Cookie(sessionID=self.sesID, md5=self.md5)

        self.LoginClt = LoginClient()
        self.data = ['On3L1n', 'On3L1nn']

    def test_LOGIN_AUTH_12(self):
        resBodyLst = []
        for item in self.data:
            md5 = self.ClientSes.Calculate_md5(sessionID=self.sesID, conStr=item, salt=self.salt)
            cookie = self.ClientSes.Create_Cookie(sessionID=self.sesID,  md5=md5)
            resBody = self.LoginClt.login(cookie).body
            resBodyLst.append(resBody)
        self.LoginClt.assert_login_list(resBodyLst,
                                       self.exp['code'],
                                       self.exp['msg'])

