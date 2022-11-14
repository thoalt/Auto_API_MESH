import time
import pytest
from APIObject.serviceAPI import portforwardCreateEditClient

@pytest.mark.usefixtures("login")
class Test_portEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code":0 , "msg": "Success"}
        self.portEditClt = portforwardCreateEditClient()
        self.idx = 1
        self.wanIndex = 3
        self.protocol = "TCP"
        self.startRePort = 5
        self.ipAddr = "192.168.1.3"
        self.startLoPort = 10

    @pytest.mark.success
    def test_portEdit_RES_1(self):
        time.sleep(self.timeOut)
        pload = self.portEditClt.Create_portforwardEdit_Pload(ruleIndex=self.idx, wanIndex=self.wanIndex,
                                                                  protocol=self.protocol, startRemotePort=self.startRePort,
                                                                  ipAddr=self.ipAddr, startLocalPort=self.startLoPort)
        resBody = self.portEditClt.portforwardCreateEdit(self.cookie, pload=pload).body
        self.portEditClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])

