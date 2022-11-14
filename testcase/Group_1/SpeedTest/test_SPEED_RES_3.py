import time

import pytest
from assertpy import assert_that

from APIObject.speedtest import SpeedTestClient


@pytest.mark.usefixtures("login")
class Test_SpeedTest():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 610
        self.exp = {"code": 15, "msg": "Session Timeout"}

        self.SpeedtClt = SpeedTestClient()
    def test_SPEED_RES_3(self):
        time.sleep(self.timeOut)
        resBody = self.SpeedtClt.speedtest(self.cookie).body
        self.SpeedtClt.assert_speedtest(resBody,
                                    self.exp['code'],
                                    self.exp['msg'])