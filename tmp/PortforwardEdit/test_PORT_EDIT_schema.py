import time
import pytest
from APIObject.serviceAPI import portforwardCreateEditClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_portCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "portforwardEdit"}
        self.portCreateClt = portforwardCreateEditClient()
        self.idx = 1
        self.wanIndex = "1"
        self.protocol = "TCP"
        self.startRePort = "1"
        self.ipAddr = "192.168.1.5"
        self.startLoPort = "1"

    @pytest.mark.success
    def test_portCreate_RES_1(self):
        time.sleep(self.timeOut)
        pload = self.portCreateClt.Create_portforwardCreate_pload(ruleIndex=self.idx, wanIndex=self.wanIndex,
                                                                  protocol=self.protocol, startRemotePort=self.startRePort,
                                                                  ipAddr=self.ipAddr, startLocalPort=self.startLoPort
                                                                  )
        resBody = self.portCreateClt.portforwardCreateEdit(self.cookie, pload=pload).body
        self.portCreateClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

        self.portCreateClt.valid_schema_common(resBody)
