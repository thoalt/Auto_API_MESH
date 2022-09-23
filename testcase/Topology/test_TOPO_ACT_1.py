import time
import pytest
from APIObject.topology import topologyClient


@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "topology"}
        self.topoClt = topologyClient()

    @pytest.mark.success
    def test_TOPO_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.topoClt.topology(self.cookie).body
        self.topoClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])