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

        self.SpeedtClt = SpeedTestClient()

    @pytest.mark.success
    def test_SPEED_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.SpeedtClt.speedtest(self.cookie).body
        self.SpeedtClt.assert_speedtest(resBody,
                                    self.exp['code'],
                                    self.exp['msg'],
                                    self.exp['action'],
                                    self.exp['speedCode'])