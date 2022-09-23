import json
import time

import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.ping import PingClient

@pytest.mark.usefixtures("create_shell")
class Test_Ping():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "ping"}
        self.data = "8.8.8.8"
        SSHSes = SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.LoginCtl = LoginClient()
        self.PingClt = PingClient()

        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        self.LoginCtl.login(self.cookie)


    def test_PING_RES_RESULT_2(self):

        time.sleep(self.timeOut)
        pload = self.PingClt.Create_Ping_Pload(host=self.data)
        resBody = self.PingClt.ping(self.cookie, pload).body
        self.PingClt.assert_ping(resBody,
                                self.exp['code'],
                                self.exp['msg'],
                                self.exp['action'])

        result = self.PingClt.get_result(resBody)
        self.PingClt.assert_result(result, pingCode=3, host=self.data, cntFail=10)
        print(json.dumps(result, indent=4))

