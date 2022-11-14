import time
import pytest
from APIObject.serviceAPI import portforwardCreateEditClient

@pytest.mark.usefixtures("login")
class Test_portCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 610
        self.exp = {"code":0 , "msg": "Success"}
        self.portCreateClt = portforwardCreateEditClient()
        self.idx = 1
        self.wanIndex = ""
        self.protocol = ""
        self.startRePort = ""
        self.ipAddr = ""
        self.startLoPort = ""

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
                                        self.exp['msg'])

