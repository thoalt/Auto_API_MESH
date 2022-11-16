import time
import pytest
from APIObject.lanAPI import LanEditClient
from base.SerialLib import Serial_Lib

@pytest.mark.usefixtures("login")
class Test_Lan_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success"}
        self.laneditClt = LanEditClient()
        # self.ipAddr = ['192.168.66.1', '1.1.1.1', '10.10.10.10']
        self.ipAddr = ['192.168.66.1']
        self.netMark = '255.255.255.0'

    @pytest.mark.skip(reason="This is Manual Testcase")
    def test_LANEDIT_RES_1(self):
        for item in self.ipAddr:
            # serialClt = Serial_Lib()

            time.sleep(self.timeOut)
            pload = self.laneditClt.Create_LanEdit_Payload(ipAddr=item, netMask=self.netMark)
            resBody = self.laneditClt.lanEdit(self.cookie, pload=pload).body
            self.laneditClt.assert_response(resBody,
                                            self.exp['code'],
                                            self.exp['msg'])
            time.sleep(30)

            # serialClt.Reset_Factory()
            # serialClt.Close_Serial_Connect()
            # del serialClt