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
        self.timeOut = 590
        self.exp = {"code": 0, "msg": "Success", "action": "ping"}

        SSHSes = SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.LoginCtl = LoginClient()
        self.PingClt = PingClient()

        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        self.LoginCtl.login(self.cookie)


    def test_PING_RES_2(self):
        time.sleep(self.timeOut)
        pload = self.PingClt.Create_Ping_Pload(host="8.8.8.8")
        resBody = self.PingClt.ping(self.cookie, pload).body
        self.PingClt.assert_ping(resBody,
                                self.exp['code'],
                                self.exp['msg'],
                                self.exp['action'])

