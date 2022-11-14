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
        self.timeOut = 610
        self.exp = {"code": 15, "msg": "Session Timeout"}


        self.PingClt = PingClient()
    def test_PING_RES_3(self):
        time.sleep(self.timeOut)
        pload = self.PingClt.Create_Ping_Pload(host="8.8.8.8")
        resBody = self.PingClt.ping(self.cookie, pload).body
        self.PingClt.assert_ping(resBody,
                                 self.exp['code'],
                                 self.exp['msg'])

