import time
import pytest
from APIObject.getWifiList import getWifiListClient

@pytest.mark.usefixtures("login")
class Test_getWifi():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "getWifiList"}

        self.getWifiClt = getWifiListClient()

    def test_getWifi_ACT_1(self):
        time.sleep(self.timeOut)
        response = self.getWifiClt.getWifiList(self.cookie)
        resBody = response.body
        self.getWifiClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])