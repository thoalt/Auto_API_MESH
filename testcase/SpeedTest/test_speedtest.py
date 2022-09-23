import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.speedtest import SpeedTestClient


@pytest.mark.usefixtures("create_shell")
class Test_SpeedTest():
    sesID, salt = "", ""
    reqID = 0

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        SSHSes = SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.LoginClt = LoginClient()
        self.SpeedtClt = SpeedTestClient()

        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        print("***************** COOKIE **************")
        print(self.cookie)

        self.LoginClt.login(self.cookie)

    @pytest.mark.success
    def test_speedtest_success(self):
        resBody = self.SpeedtClt.speedtest(self.cookie).body
        print(resBody)