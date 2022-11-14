import time
import pytest
from APIObject.serviceAPI import portforwardCreateEditClient

@pytest.mark.usefixtures("login")
class Test_portCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 10, "msg": "Miss Attribute"}
        self.portCreateClt = portforwardCreateEditClient()
        self.idx = 1
        self.wanIndex = "2"
        self.protocol = "TCP"
        self.startRePort = "1"
        self.ipAddr = "192.168.1.5"
        self.startLoPort = "1"
        self.serviceName = "abc"
        pload = self.portCreateClt.Create_portforwardCreate_pload()
        self.data = self.portCreateClt.Remove_Attribute_In_Pload(pload)

    def test_portCreate_RES_1(self):
        time.sleep(self.timeOut)
        pload = self.portCreateClt.Create_portforwardCreate_pload(ruleIndex=self.idx, wanIndex=self.wanIndex,
                                                                  protocol=self.protocol, startRemotePort=self.startRePort,
                                                                  ipAddr=self.ipAddr, startLocalPort=self.startLoPort,
                                                                  serviceName=self.serviceName)
        resBody = self.portCreateClt.portforwardCreateEdit(self.cookie, pload=pload).body
        self.portCreateClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])

