import time
import pytest
from APIObject.getWifiList import getWifiListClient

@pytest.mark.usefixtures("login")
class Test_getWifi():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 11, "msg": "Verify Fail"}

        self.getWifiClt = getWifiListClient()
        self.data = ['', -1, 1.12, 2147483648, 'abc']

    def test_getWifi_ACT_1(self):
        resBodyLst = []
        for item in self.data:
            time.sleep(self.timeOut)
            pload = self.getWifiClt.Create_getWifiList_Pload(reqID=item)
            resBody = self.getWifiClt.getWifiList(cookies=self.cookie, pload=pload).body
            resBodyLst.append(resBody)
        self.getWifiClt.assert_response_list(resBodyLst,
                                        self.exp['code'],
                                        self.exp['msg'])