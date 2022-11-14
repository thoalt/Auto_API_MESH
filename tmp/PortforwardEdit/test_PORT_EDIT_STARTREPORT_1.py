import time
import pytest
from APIObject.serviceAPI import portforwardCreateEditClient

@pytest.mark.usefixtures("login")
class Test_portCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 0, "msg": "Success"}
        self.portCreateClt = portforwardCreateEditClient()
        self.idx = 1
        self.wanIndex = 1
        self.protocol = "TCP"
        #self.startRePort = 1
        self.ipAddr = "192.168.1.5"
        self.startLoPort = 1
        self.data = [1, 32768, 65535]

    def test_portCreate_index_1(self):
        resBody_lst = []
        for item in self.data:
           pload = self.portCreateClt.Create_portforwardCreate_pload(wanIndex=self.wanIndex,
                                                                  protocol=self.protocol, startRemotePort=item,
                                                                  ipAddr=self.ipAddr, startLocalPort=self.startLoPort,
                                                                  ruleIndex=self.idx)
           resBody = self.portCreateClt.portforwardCreateEdit(self.cookie, pload=pload).body
           time.sleep(self.timeOut)
           resBody_lst.append(resBody)
        self.portCreateClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])



