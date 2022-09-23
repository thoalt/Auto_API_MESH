import time
import pytest
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.wanViewConfig import WanViewClient


@pytest.mark.usefixtures("login")
class Test_Wanview():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "wanViewConfig"}
        self.WanviewClt = WanViewClient()

        # self.ClientSes = openssesionClient()
        # self.LoginClt = LoginClient()
        #
        #
        # self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        # self.LoginClt.login(self.cookie)

    @pytest.mark.success
    def test_WANVIEW_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.WanviewClt.wanViewConfig(self.cookie).body
        self.WanviewClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])