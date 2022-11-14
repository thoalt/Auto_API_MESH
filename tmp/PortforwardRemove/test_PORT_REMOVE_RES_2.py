import time
import pytest
from APIObject.serviceAPI import portforwardRemoveClient

@pytest.mark.usefixtures("login")
class Test_portRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 590
        self.exp = {"code":0 , "msg": "Success"}
        self.portRemoveClt = portforwardRemoveClient()
        self.idx = 1

    @pytest.mark.success
    def test_portRemove_RES_2(self):
        time.sleep(self.timeOut)
        pload = self.portRemoveClt.Create_portforwardRemove_Pload(ruleIndex=self.idx)
        resBody = self.portRemoveClt.portforwardRemove(self.cookie, pload=pload).body
        self.portRemoveClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])

