import time
import pytest
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.lanAPI import LanViewClient


@pytest.mark.usefixtures("login")
class Test_LanView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 10, "msg": "Miss Attribute"}
        self.LanviewClt = LanViewClient()
        pload = self.LanviewClt.Create_LanView_Pload()
        self.data = [self.LanviewClt.Remove_Key_In_Pload(pload, 'action')]

    def test_LANVIEW_ACT_2(self):
        time.sleep(self.timeOut)
        resbody_Lst = []
        for item in self.data:
            resBody = self.LanviewClt.lanView(cookies=self.cookie, pload=item).body
            resbody_Lst.append(resBody)

        self.LanviewClt.assert_response_list(resbody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])