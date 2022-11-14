import time
import pytest
from APIObject.topology import topologyClient


@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ["“", "‘", "|", "/", "\\", ",", ";", ":", "&", "<", ">", "^", "*", "?"]
        self.topoClt = topologyClient()

    def test_TOPO_ACT_1(self):
        resBody_lst = []
        time.sleep(self.timeOut)
        for item in self.data:
            pload = self.topoClt.Create_topology_Pload(action=item)
            resBody = self.topoClt.topology(self.cookie, pload).body
            resBody_lst.append(resBody)
        self.topoClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])
