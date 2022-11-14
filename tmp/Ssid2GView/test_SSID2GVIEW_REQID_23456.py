import time
import pytest
from APIObject.wifi24GAPI import ssid24GViewClient

@pytest.mark.usefixtures("login")
class Test_ssid24GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code":11 , "msg": "Verify Fail"}
        self.ssid24GViewClt = ssid24GViewClient()
        self.data = ['', -1, 1.24, 2147483648, 'abc']


    def test_ssid24GView_reqID_23456(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.ssid24GViewClt.Create_ssid24GView_Pload(reqID=item)
            resBody = self.ssid24GViewClt.ssid24GView(self.cookie, pload).body
            resBody_lst.append(resBody)
        self.ssid24GViewClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])




