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
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.data = [2147483648]

        SSHSes = SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.LoginClt = LoginClient()
        self.LanviewClt = LanViewClient()

        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        self.LoginClt.login(self.cookie)


    def test_LANVIEW_REQID_5(self):
        time.sleep(self.timeOut)
        resbody_Lst = []
        for item in self.data:
            pload = self.LanviewClt.Create_LanView_Pload(reqID=item)
            resBody = self.LanviewClt.lanView(cookies=self.cookie, pload=pload).body
            resbody_Lst.append(resBody)

        self.LanviewClt.assert_response_list(resbody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])