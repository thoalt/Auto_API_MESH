import time
import pytest
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.lanAPI import LanViewClient


@pytest.mark.usefixtures("create_shell")
class Test_LanView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 610
        self.exp = {"code": 15, "msg": "Session Timeout"}


        SSHSes = SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.LoginClt = LoginClient()
        self.LanviewClt = LanViewClient()

        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        self.LoginClt.login(self.cookie)

    @pytest.mark.success
    def test_LANVIEW_RES_3(self):
        time.sleep(self.timeOut)
        response = self.LanviewClt.lanView(self.cookie)
        resBody = response.body
        self.LanviewClt.assert_response(resBody,
                                        self

                                        .exp['code'],
                                        self.exp['msg'],)