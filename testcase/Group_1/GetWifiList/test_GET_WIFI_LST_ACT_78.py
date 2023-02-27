import time
import pytest
from APIObject.getWifiList import getWifiListClient

@pytest.mark.usefixtures("login")
class Test_getWifi():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}

        self.getWifiClt = getWifiListClient()
        self.data = ["“", "‘", "|", "/", "\\", ",", ";", ":", "&", "<", ">","!", "^", "*", "?", "ă", "â",
                     "đ", "ê", "ô", "ơ", "ư", "á", "à", "ạ", "ả", "ã",
                    "Ă", "Â", "Đ", "Ê", "Ô", "Ơ", "Ư", "Á", "À", "Ạ", "Ả", "Ã", "getWifiList ",
                     " getWifiList", "get WifiList"]

    def test_getWifi_ACT_1(self):
        resBodyLst = []
        for item in self.data:
            time.sleep(self.timeOut)
            pload = self.getWifiClt.Create_getWifiList_Pload(action=item)
            resBody = self.getWifiClt.getWifiList(cookies=self.cookie, pload=pload).body
            resBodyLst.append(resBody)
        self.getWifiClt.assert_response_list(resBodyLst,
                                        self.exp['code'],
                                        self.exp['msg'])