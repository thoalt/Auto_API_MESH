import time
import pytest
from APIObject.serviceAPI import portforwardCreateEditClient

@pytest.mark.usefixtures("login")
class Test_portCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.portCreateClt = portforwardCreateEditClient()
        self.idx = 1
        self.wanIndex = "1"
        self.protocol = "TCP"
        self.startRePort = "1"
        self.ipAddr = "192.168.1.5"
        self.startLoPort = "1"
        self.serviceName = "abc"
        self.data = ["“", "‘", "|", "/", "\\", ",", ";", ":", "&", "<", ">", "^", "*", "?", "ă", "â",
                     "đ", "ê", "ô", "ơ", "ư", "á", "à", "ạ", "ả", "ã",
                    "Ă", "Â", "Đ", "Ê", "Ô", "Ơ", "Ư", "Á", "À", "Ạ", "Ả", "Ã", "portforward Create",
                     " portforwardCreate", "portforwardCreate  "]

    def test_portCreate_ACT_678(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
           pload = self.portCreateClt.Create_portforwardCreate_pload(ruleIndex=self.idx, wanIndex=self.wanIndex,
                                                                  protocol=self.protocol, startRemotePort=self.startRePort,
                                                                  ipAddr=self.ipAddr, startLocalPort=self.startLoPort,
                                                                  serviceName=self.serviceName, action=item)
           resBody = self.portCreateClt.portforwardCreateEdit(self.cookie, pload=pload).body
           resBody_lst.append(resBody)
        self.portCreateClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])


