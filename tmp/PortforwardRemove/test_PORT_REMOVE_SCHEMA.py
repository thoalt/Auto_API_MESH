import time
import pytest
from APIObject.serviceAPI import portforwardRemoveClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_portRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "portforwardRemove"}
        self.portRemoveClt = portforwardRemoveClient()
        self.idx = 2

    @pytest.mark.success
    def test_portRemove_ACT_1(self):
        time.sleep(self.timeOut)
        pload = self.portRemoveClt.Create_portforwardRemove_Pload(ruleIndex=self.idx)
        resBody = self.portRemoveClt.portforwardRemove(self.cookie, pload=pload).body
        self.portRemoveClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
        self.portRemoveClt.valid_schema_common(resBody)


