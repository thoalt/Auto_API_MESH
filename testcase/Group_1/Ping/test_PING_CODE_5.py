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
        self.data = ["ă", "â", "đ", "ê", "ô", "ơ", "ư", "á", "à", "ạ", "ả", "ã",
                     "Ă", "Â", "Đ", "Ê", "Ô", "Ơ", "Ư", "Á", "À", "Ạ", "Ả", "Ã"]

        self.PingClt = PingClient()
    def test_PING_RES_1(self):
        time.sleep(self.timeOut)
        resbody_Lst = []
        for item in self.data:
            pload = self.PingClt.Create_Ping_Pload(pingCode=item, host=self.host)
            resBody = self.PingClt.ping(cookies=self.cookie, pload=pload).body
            resbody_Lst.append(resBody)
        self.PingClt.assert_ping_lst(resbody_Lst,
                                self.exp['code'],
                                self.exp['msg'])
