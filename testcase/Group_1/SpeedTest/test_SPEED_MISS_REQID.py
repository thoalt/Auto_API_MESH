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
        self.timeOut = 5
        self.exp = {"code": 9, "msg": "Miss Request ID"}


        self.SpeedtClt = SpeedTestClient()
        pload = self.SpeedtClt.Create_SpeedTest_Pload()
        self.data = [self.SpeedtClt.Remove_Key_In_Pload(pload, 'requestId')]

    def test_SPEED_ACT_2(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:

            resBody = self.SpeedtClt.speedtest(cookies=self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
        self.SpeedtClt.assert_speedtest_lst(resBody_Lst,
                                    self.exp['code'],
                                    self.exp['msg'])