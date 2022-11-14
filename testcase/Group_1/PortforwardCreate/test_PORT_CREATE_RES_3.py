import time
import pytest
from APIObject.serviceAPI import portforwardCreateEditClient, portforwardRemoveClient, portforwardViewClient

@pytest.mark.usefixtures("login")
class Test_portCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 610
        self.exp = {"code": 15, "msg": "Session Timeout"}
        self.portCreateClt = portforwardCreateEditClient()
        self.portViewClient = portforwardViewClient()
        self.portViewClient.portforwardView(self.cookie)
        self.portRemoveClt = portforwardRemoveClient()
        self.portRemoveClt.remove_all_port(self.cookie)
        self.idx = 0
        self.wanIndex = 0
        self.protocol = "UDP"
        self.startRePort = 1
        self.ipAddr = "192.168.4.5"
        self.startLoPort = 1
        self.serviceName = "name"


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

