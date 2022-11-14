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
        self.exp = {"code": 10, "msg": "Miss Attribute"}
        self.host = "8.8.8.8"
        self.PingClt = PingClient()

        pload = self.PingClt.Create_Ping_Pload(host=self.host)
        self.data = self.PingClt.Remove_Attribute_In_Pload(pload)

    def test_PING_RES_1(self):
        time.sleep(self.timeOut)
        resbody_Lst = []
        for item in self.data:
            resBody = self.PingClt.ping(cookies=self.cookie,pload=item).body
            resbody_Lst.append(resBody)
        self.PingClt.assert_ping_lst(resbody_Lst,
                                self.exp['code'],
                                self.exp['msg'])
