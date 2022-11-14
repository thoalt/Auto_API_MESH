import time
import pytest
from APIObject.serviceAPI import portforwardRemoveClient

@pytest.mark.usefixtures("login")
class Test_portRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.portRemoveClt = portforwardRemoveClient()
        #self.idx = 2
        self.data = ['', -1, 1.12, 8, 'abc']

    def test_portRemove_INDEX_23456(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
           pload = self.portRemoveClt.Create_portforwardRemove_Pload(ruleIndex=item)
           resBody = self.portRemoveClt.portforwardRemove(self.cookie, pload=pload).body
           resBody_lst.append(resBody)
        self.portRemoveClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])

