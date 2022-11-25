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
        self.data = ['getWifiList1', 'getWifiLis', 'GetWifiList',
                     'GETWIFILIST', 'getwifilist','getWifiList122144124141241241241']

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