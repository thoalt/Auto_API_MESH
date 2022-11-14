import time
import pytest
from APIObject.wifi24GAPI import ssid24GViewClient

@pytest.mark.usefixtures("login")
class Test_ssid24GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 610
        self.exp = {"code":15, "msg": "Session Timeout"}
        self.ssid24GViewClt = ssid24GViewClient()

    def test_ssid24GView_RES_3(self):
        time.sleep(self.timeOut)
        resBody = self.ssid24GViewClt.ssid24GView(self.cookie).body
        self.ssid24GViewClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])


