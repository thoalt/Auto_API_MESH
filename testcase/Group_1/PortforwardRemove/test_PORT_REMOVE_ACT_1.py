import time
import pytest
from APIObject.serviceAPI import portforwardRemoveClient, portforwardCreateEditClient

@pytest.mark.usefixtures("login")
class Test_portRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "portforwardRemove"}
        self.portCreateClt = portforwardCreateEditClient()
        self.portRemoveClt = portforwardRemoveClient()
        self.idx = 0

        self.portCreateClt.portForward_Create_Default(cookie=self.cookie)

    def test_portRemove_ACT_1(self):
        time.sleep(self.timeOut)
        pload = self.portRemoveClt.Create_portforwardRemove_Pload(ruleIndex=self.idx)
        resBody = self.portRemoveClt.portforwardRemove(self.cookie, pload=pload).body
        self.portRemoveClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])

