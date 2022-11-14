import time
import pytest
from APIObject.serviceAPI import portforwardCreateEditClient, portforwardRemoveClient, portforwardViewClient

@pytest.mark.usefixtures("login")
class Test_portCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "portforwardCreate"}
        self.portCreateClt = portforwardCreateEditClient()
        self.portViewClient = portforwardViewClient()
        self.portViewClient.portforwardView(self.cookie)
        self.portRemoveClt = portforwardRemoveClient()
        self.portRemoveClt.remove_all_port(self.cookie)
        self.idx = 0
        self.wanIndex = 0
        self.protocol = "TCP"
        self.startRePort = 1
        self.ipAddr = "192.168.1.5"
        self.startLoPort = 1
        self.serviceName = "abc"
        self.data = [0, 1, 2147483646, 2147483647]

    def test_portCreate_REQID_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for idx, item in enumerate(self.data):
           pload = self.portCreateClt.Create_portforwardCreate_pload(ruleIndex=idx, wanIndex=self.wanIndex,
                                                                  protocol=self.protocol, startRemotePort=self.startRePort,
                                                                  ipAddr=self.ipAddr, startLocalPort=self.startLoPort,
                                                                  serviceName=self.serviceName, reqID=item)
           resBody = self.portCreateClt.portforwardCreateEdit(self.cookie, pload=pload).body
           resBody_lst.append(resBody)
        self.portCreateClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])



