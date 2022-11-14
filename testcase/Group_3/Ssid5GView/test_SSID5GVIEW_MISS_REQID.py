import time
import pytest
from APIObject.wifi5GAPI import ssid5GViewClient

@pytest.mark.usefixtures("login")
class Test_ssid5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code":9 , "msg": "Miss Request ID"}
        self.ssid5GViewClt = ssid5GViewClient()
        pload = self.ssid5GViewClt.Create_ssid5GView_Pload()
        self.data = self.ssid5GViewClt.Remove_Request_ID_In_Pload(pload)

    def test_ssid5GView_miss_ATTB(self):
        time.sleep(self.timeOut)
        resBody_lst =[]
        for item in self.data:
            resBody = self.ssid5GViewClt.ssid5GView(self.cookie, pload=item).body
            resBody_lst.append(resBody)
        self.ssid5GViewClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])


