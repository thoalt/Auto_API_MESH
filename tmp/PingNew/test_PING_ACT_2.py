import json
import time

import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.ping import PingClient

@pytest.mark.usefixtures("login")
class Test_Ping():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.host = "8.8.8.8"
        self.data = ['ping1', 'pin']
        self.PingClt = PingClient()


    def test_PING_RES_1(self):
        time.sleep(self.timeOut)
        resbody_Lst = []
        for item in self.data:
            pload = self.PingClt.Create_Ping_Pload(action=item, host=self.host)
            resBody = self.PingClt.ping(cookies=self.cookie,pload=pload).body
            resbody_Lst.append(resBody)
        self.PingClt.assert_ping_lst(resbody_Lst,
                                self.exp['code'],
                                self.exp['msg'])
