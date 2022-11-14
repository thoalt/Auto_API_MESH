import time
import pytest
from APIObject.topology import topologyClient


@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 10, "msg": "Miss Attribute"}

        self.topoClt = topologyClient()
        pload = self.topoClt.Create_topology_Pload()
        self.data = [self.topoClt.Remove_Key_In_Pload(pload, 'action')]

    def test_TOPO_ACT_1(self):
        resBody_lst = []
        time.sleep(self.timeOut)
        for item in self.data:
            resBody = self.topoClt.topology(self.cookie, item).body
            resBody_lst.append(resBody)
        self.topoClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])
