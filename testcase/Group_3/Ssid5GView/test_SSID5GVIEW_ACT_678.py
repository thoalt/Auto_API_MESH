import time
import pytest
from APIObject.wifi5GAPI import ssid5GViewClient

@pytest.mark.usefixtures("login")
class Test_ssid5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code":8, "msg": "Invalid Action"}
        self.ssid5GViewClt = ssid5GViewClient()
        self.data = ["“", "‘", "|", "/", "\\", ",", ";", ":", "&", "<", ">", "^", "*", "?", "ă", "â", "đ",
                     "ê", "ô", "ơ", "ư", "á", "à", "ạ", "ả", "ã",
                    "Ă", "Â", "Đ", "Ê", "Ô", "Ơ", "Ư", "Á", "À", "Ạ", "Ả", "Ã"]

    def test_ssid5GView_ACT_678(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.ssid5GViewClt.Create_ssid5GView_Pload(action=item)
            resBody = self.ssid5GViewClt.ssid5GView(self.cookie, pload).body
            resBody_lst.append(resBody)
        self.ssid5GViewClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])


