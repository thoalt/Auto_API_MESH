import time

import pytest
from assertpy import assert_that

from APIObject.login import LoginClient
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.logout import LogoutClient
from Utilities import Utility as utl

@pytest.mark.usefixtures("create_shell")
class Test_Logout():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        SSHSes=SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.LoginCtl = LoginClient()
        self.LogoutClt = LogoutClient()

        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        print("***************** COOKIE **************")
        print(self.cookie)

        self.LoginCtl.login(self.cookie)

        time.sleep(10)

    @pytest.mark.success
    def test_Logout_Success(self):
        resBody = self.LogoutClt.logout(self.cookie).body
        self.LogoutClt.assert_logout(resBody, 0, "Success", "logout")
