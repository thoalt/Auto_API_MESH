import time
import pytest
from APIObject.serviceAPI import portforwardRemoveClient

@pytest.mark.usefixtures("login")
class Test_portRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 10, "msg": "Miss Attribute"}
        self.portRemoveClt = portforwardRemoveClient()
        self.idx = 2
        pload = self.portRemoveClt.Create_portforwardRemove_Pload()
        self.data = self.portRemoveClt.Remove_Attribute_In_Pload(pload)

    def test_portRemove_MISS_ATTB(self):
        time.sleep(self.timeOut)
        pload = self.portRemoveClt.Create_portforwardRemove_Pload(ruleIndex=self.idx)
        resBody = self.portRemoveClt.portforwardRemove(self.cookie, pload=pload).body
        self.portRemoveClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])

