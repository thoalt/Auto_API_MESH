import time
import pytest
from APIObject.wifi24GAPI import radio24GViewClient


@pytest.mark.usefixtures("login")
class Test_Radio2GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "radio2.4GView"}
        self.radio2G = radio24GViewClient()


    @pytest.mark.success
    def test_RADIO_2G_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.radio2G.radio24GView(self.cookie).body
        self.radio2G.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])