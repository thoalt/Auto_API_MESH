import time
import pytest
from APIObject.serviceAPI import portforwardRemoveClient, portforwardViewClient

@pytest.mark.usefixtures("login")
class Test_portRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success"}
        self.portViewClient = portforwardViewClient()
        self.portViewClient.portforwardView(self.cookie)
        self.portRemoveClt = portforwardRemoveClient()
        #self.idx = 2
        self.data = [7, 6, 5, 4, 3, 2, 1, 0]

    def test_portRemove_INDEX_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
           pload = self.portRemoveClt.Create_portforwardRemove_Pload(ruleIndex=item)
           resBody = self.portRemoveClt.portforwardRemove(self.cookie, pload=pload).body
           resBody_lst.append(resBody)
           time.sleep(30)
        self.portRemoveClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])

