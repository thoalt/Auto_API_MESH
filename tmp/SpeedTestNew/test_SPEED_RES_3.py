import time

import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.speedtest import SpeedTestClient


@pytest.mark.usefixtures("login")
class Test_SpeedTest():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 610
        self.exp = {"code": 15, "msg": "Session Timeout"}

        SSHSes = SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.LoginClt = LoginClient()
        self.SpeedtClt = SpeedTestClient()

        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        self.LoginClt.login(self.cookie)

    def test_SPEED_RES_3(self):
        time.sleep(self.timeOut)
        resBody = self.SpeedtClt.speedtest(self.cookie).body
        self.SpeedtClt.assert_speedtest(resBody,
                                    self.exp['code'],
                                    self.exp['msg'])