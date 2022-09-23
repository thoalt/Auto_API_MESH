import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from Utilities import Utility as utl

@pytest.mark.usefixtures("create_shell")
class Test_Login():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):

        self.exp = {"code": 12, "msg": "Unknown Error"}

        SSHSes=SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.sesID, self.salt, self.reqID = self.ClientSes.Open_Session_And_Get_Session_ID()

        self.md5 = self.ClientSes.Calculate_md5(sessionID=self.sesID, salt=self.salt)
        self.cookie = self.ClientSes.Create_Cookie(sessionID=self.sesID, md5=self.md5)

        self.LoginClt = LoginClient()
        self.data = [": " + self.cookie]


    def test_LOGIN_COOKIE_2(self):
        resBodyLst = []
        for item in self.data:
            resBody = self.LoginClt.login(item).body
            resBodyLst.append(resBody)
        self.LoginClt.assert_login_list(resBodyLst,
                                       self.exp['code'],
                                       self.exp['msg'])

