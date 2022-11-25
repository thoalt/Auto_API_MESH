import time
import pytest
from APIObject.getWifiList import getWifiListClient

@pytest.mark.usefixtures("login")
class Test_getWifi():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 10, "msg": "Miss Attribute"}

        self.getWifiClt = getWifiListClient()
        pload = self.getWifiClt.Create_getWifiList_Pload()
        self.data = self.getWifiClt.Remove_Attribute_In_Pload(dictBefore=pload)

    def test_getWifi_ACT_1(self):
        resBodyLst = []
        for item in self.data:
            time.sleep(self.timeOut)
            resBody = self.getWifiClt.getWifiList(cookies=self.cookie, pload=item).body
            resBodyLst.append(resBody)
        self.getWifiClt.assert_response_list(resBodyLst,
                                        self.exp['code'],
                                        self.exp['msg'])