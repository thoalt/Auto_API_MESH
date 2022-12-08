import time
import pytest
from APIObject.lanAPI import LanEditClient


@pytest.mark.usefixtures("login")
class Test_Lan_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success"}
        self.laneditClt = LanEditClient()
        self.ipAddr = '192.168.66.1'
        self.netMark = ['255.255.255.0', '255.255.0.0', '255.0.0.0']

    # @pytest.mark.skip(reason="This is Manual Testcase")
    def test_LANEDIT_RES_1(self):
        for item in self.netMark:
            time.sleep(self.timeOut)
            pload = self.laneditClt.Create_LanEdit_Payload(ipAddr=self.ipAddr, netMask=item)
            resBody = self.laneditClt.lanEdit(self.cookie, pload=pload).body
            self.laneditClt.assert_response(resBody,
                                            self.exp['code'],
                                            self.exp['msg'])