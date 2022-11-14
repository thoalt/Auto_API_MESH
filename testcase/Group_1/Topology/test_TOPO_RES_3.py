import time
import pytest
from APIObject.topology import topologyClient
from Config import Schema_Template as scTmp


@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 610
        self.exp = {"code": 15, "msg": "Session Timeout"}
        self.topoClt = topologyClient()

    def test_TOPO_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.topoClt.topology(self.cookie).body
        self.topoClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
