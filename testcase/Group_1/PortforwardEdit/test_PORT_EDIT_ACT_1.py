import time
import pytest
from APIObject.serviceAPI import portforwardCreateEditClient

@pytest.mark.usefixtures("login")
class Test_portCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "portforwardEdit"}
        self.portCreateClt = portforwardCreateEditClient()
        #self.portViewClient = portforwardViewClient()
        #self.portViewClient.portforwardView(self.cookie)
        #self.portRemoveClt = portforwardRemoveClient()
        #self.portRemoveClt.remove_all_port(self.cookie)
        self.idx = 0
        self.wanIndex = 0
        self.protocol = "TCP"
        self.startRePort = 1
        self.ipAddr = "192.168.1.10"
        self.startLoPort = 1

    def test_portedit_act_1(self):
        time.sleep(self.timeOut)
        pload = self.portCreateClt.Create_portforwardEdit_Pload(ruleIndex=self.idx, wanIndex=self.wanIndex,
                                                                  protocol=self.protocol, startRemotePort=self.startRePort,
                                                                  ipAddr=self.ipAddr, startLocalPort=self.startLoPort,
                                                                  )
        resBody = self.portCreateClt.portforwardCreateEdit(self.cookie, pload=pload).body
        self.portCreateClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

