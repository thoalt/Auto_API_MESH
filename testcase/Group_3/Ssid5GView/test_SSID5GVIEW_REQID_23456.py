import time
import pytest
from APIObject.wifi5GAPI import ssid5GViewClient

@pytest.mark.usefixtures("login")
class Test_ssid5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code":11, "msg": "Verify Fail"}
        self.ssid5GViewClt = ssid5GViewClient()
        self.data = ['', -1, 1.34, 2147483648, 'abc']

    def test_ssid5GView_ACT_2345(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.ssid5GViewClt.Create_ssid5GView_Pload(reqID=item)
            resBody = self.ssid5GViewClt.ssid5GView(self.cookie, pload).body
            resBody_lst.append(resBody)
        self.ssid5GViewClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])


