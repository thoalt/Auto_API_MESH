import json
import time

import pytest
from assertpy import assert_that

from APIObject.ping import PingClient

@pytest.mark.usefixtures("login")
class Test_Ping():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.host = "8.8.8.8"
        self.data = [" 8.8.8.8", "8.8.8.8 ", "8.8 .8.8",
                     " google.com.vn", "google.com.vn ", "google.com .vn"]


        self.PingClt = PingClient()
    def test_PING_RES_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.PingClt.Create_Ping_Pload(host=item)
            resBody = self.PingClt.ping(self.cookie, pload).body
            resBody_lst.append(resBody)

        self.PingClt.assert_ping_lst(resBody_lst,
                                    self.exp['code'],
                                    self.exp['msg'])
