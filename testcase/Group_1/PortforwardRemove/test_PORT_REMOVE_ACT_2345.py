import time
import pytest
from APIObject.serviceAPI import portforwardRemoveClient

@pytest.mark.usefixtures("login")
class Test_portRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.portRemoveClt = portforwardRemoveClient()
        self.idx = 2
        self.data = ['portforwardRemove1', 'portforwardRemov', 'PortforwardRemove', 'PORTFORWARDREMOVE',
                     '', 'openSession122144124141241241241']

    def test_portRemove_ACT_2345(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
           pload = self.portRemoveClt.Create_portforwardRemove_Pload(ruleIndex=self.idx, action=item)
           resBody = self.portRemoveClt.portforwardRemove(self.cookie, pload=pload).body
           resBody_lst.append(resBody)
        self.portRemoveClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])

