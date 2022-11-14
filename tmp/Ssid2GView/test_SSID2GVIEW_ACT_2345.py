import time
import pytest
from APIObject.wifi24GAPI import ssid24GViewClient

@pytest.mark.usefixtures("login")
class Test_ssid24GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code":8 , "msg": "Invalid Action"}
        self.ssid24GViewClt = ssid24GViewClient()
        self.data = ["guest2.4GView1", "guest2.4GVie", "Guest2.4GView", "GUEST2.4GVIEW",'']


    def test_ssid24GView_ACT_2345(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.ssid24GViewClt.Create_ssid24GView_Pload(action=item)
            resBody = self.ssid24GViewClt.ssid24GView(self.cookie, pload).body
            resBody_lst.append(resBody)
        self.ssid24GViewClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])



