import time
import pytest
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.wanAPI import WanViewConfigClient
from APIObject.wifi5GAPI import radio5GViewClient


@pytest.mark.usefixtures("login")
class Test_Radio5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "radio5GView"}
        self.radio5G = radio5GViewClient()



    def test_RADIO_5G_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.radio5G.radio5GView(self.cookie).body
        self.radio5G.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])