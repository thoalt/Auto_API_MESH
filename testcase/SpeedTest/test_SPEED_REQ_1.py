import time

import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.speedtest import SpeedTestClient


@pytest.mark.usefixtures("create_shell")
class Test_SpeedTest():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "speedtest", "speedCode": 3}
        self.data = [0, 1, 2147483646, 2147483647]

        SSHSes = SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.LoginClt = LoginClient()
        self.SpeedtClt = SpeedTestClient()

        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        self.LoginClt.login(self.cookie)

    @pytest.mark.success
    def test_SPEED_REQ_1(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.SpeedtClt.Create_SpeedTest_Pload(reqID=item)
            resBody = self.SpeedtClt.speedtest(cookies=self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
        self.SpeedtClt.assert_speedtest_lst(resBody_Lst,
                                    self.exp['code'],
                                    self.exp['msg'],
                                    self.exp['action'],
                                    self.exp['speedCode'])