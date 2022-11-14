import time
import pytest
from APIObject.serviceAPI import portforwardCreateEditClient

@pytest.mark.usefixtures("login")
class Test_portEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success"}
        self.portEditClt = portforwardCreateEditClient()
        self.idx = 0
        self.wanIndex = 0
        self.protocol = "TCP"
        self.startRePort = 5
        self.ipAddr = "192.168.1.3"
        self.startLoPort = 10
        self.serviceName = 145

    def test_portEdit_RES_1(self):
        time.sleep(self.timeOut)
        pload = self.portEditClt.Create_portforwardEdit_Pload(ruleIndex=self.idx, wanIndex=self.wanIndex,
                                                                  protocol=self.protocol, startRemotePort=self.startRePort,
                                                                  ipAddr=self.ipAddr, startLocalPort=self.startLoPort, serviceName=self.serviceName)
        resBody = self.portEditClt.portforwardCreateEdit(self.cookie, pload=pload).body
        self.portEditClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])

