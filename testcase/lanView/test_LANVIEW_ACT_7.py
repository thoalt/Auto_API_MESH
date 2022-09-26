import time
import pytest
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.lanView import LanViewClient


@pytest.mark.usefixtures("create_shell")
class Test_LanView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ["ă", "â", "đ", "ê", "ô", "ơ", "ư", "á", "à", "ạ", "ả", "ã",
                    "Ă", "Â", "Đ", "Ê", "Ô", "Ơ", "Ư", "Á", "À", "Ạ", "Ả", "Ã"]

        SSHSes = SSH_Lib(SSHShell=self.SSHShell)
        SSHSes.start_mobile_agent()
        self.ClientSes = openssesionClient()
        self.LoginClt = LoginClient()
        self.LanviewClt = LanViewClient()

        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        self.LoginClt.login(self.cookie)


    def test_LANVIEW_ACT_7(self):
        time.sleep(self.timeOut)
        resbody_Lst = []
        for item in self.data:
            pload = self.LanviewClt.Create_LanView_Pload(action=item)
            resBody = self.LanviewClt.lanView(cookies=self.cookie, pload=pload).body
            resbody_Lst.append(resBody)

        self.LanviewClt.assert_response_list(resbody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])