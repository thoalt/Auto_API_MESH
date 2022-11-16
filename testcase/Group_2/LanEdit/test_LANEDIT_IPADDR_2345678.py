import time
import pytest
from APIObject.lanAPI import LanEditClient


@pytest.mark.usefixtures("login")
class Test_Lan_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.laneditClt = LanEditClient()
        self.ipAddr = ['8.8.8', '8.8', '8.8.8.8.8',
                       "256.1.1.1",
                       "1.256.1.1",
                       "1.1.256.1",
                       "1.1.1.256",
                       "256.255.255.255",
                       "255.256.255.255",
                       "255.255.255.256",
                       "",
                       "a.b.c.d",
                       "1,1.1.1"
                       #"127.0.0.1"
                       # "1,1.1.1",
                       # "255.255.255.255"
                       ]

        self.netMark = '255.255.255.0'

    def test_LANEDIT_RES_1(self):
        resBody_Lst = []
        for item in self.ipAddr:
            time.sleep(self.timeOut)
            pload = self.laneditClt.Create_LanEdit_Payload(ipAddr=item, netMask=self.netMark)
            resBody = self.laneditClt.lanEdit(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)

        self.laneditClt.assert_response_list(resBody_Lst,
                                            self.exp['code'],
                                            self.exp['msg'])