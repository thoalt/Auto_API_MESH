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
        self.exp = {"code": 0, "msg": "Success", "action": "ping"}
        self.data = "8.8.8.8"

        self.PingClt = PingClient()
    def test_PING_RES_RESULT_1(self):
        time.sleep(self.timeOut)
        pload = self.PingClt.Create_Ping_Pload(host=self.data)
        resBody = self.PingClt.ping(self.cookie, pload).body
        self.PingClt.assert_ping(resBody,
                                self.exp['code'],
                                self.exp['msg'],
                                self.exp['action'])

        result = self.PingClt.get_result(resBody)
        self.PingClt.assert_result(result, pingCode=3, host=self.data, cntPass=10)
        # print(json.dumps(result, indent=4))

