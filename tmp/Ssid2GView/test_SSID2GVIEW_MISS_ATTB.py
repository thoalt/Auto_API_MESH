import time
import pytest
from APIObject.wifi24GAPI import ssid24GViewClient

@pytest.mark.usefixtures("login")
class Test_ssid24GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code":10 , "msg": "Miss Atrribute"}
        self.ssid24GViewClt = ssid24GViewClient()
        pload = self.ssid24GViewClt.Create_ssid24GView_Pload()
        self.data = self.ssid24GViewClt.Remove_Attribute_In_Pload(pload)


    def test_ssid24GView_miss_ATTB(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.ssid24GViewClt.Create_ssid24GView_Pload(pload=item)
            resBody = self.ssid24GViewClt.ssid24GView(self.cookie, pload).body
            resBody_lst.append(resBody)
        self.ssid24GViewClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])



