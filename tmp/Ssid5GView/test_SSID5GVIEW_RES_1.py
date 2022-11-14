import time
import pytest
from APIObject.wifi5GAPI import ssid5GViewClient

@pytest.mark.usefixtures("login")
class Test_ssid5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code":0 , "msg": "Success", "action": "ssid5GView"}
        self.ssid5GViewClt = ssid5GViewClient()

    @pytest.mark.success
    def test_ssid5GView_RES_1(self):
        time.sleep(self.timeOut)
        resBody = self.ssid5GViewClt.ssid5GView(self.cookie).body
        self.ssid5GViewClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

