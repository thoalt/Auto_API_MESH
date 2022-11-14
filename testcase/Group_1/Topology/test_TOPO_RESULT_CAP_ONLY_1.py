import time
import pytest
from APIObject.topology import topologyClient
from Config import Schema_Template as scTmp


@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success", "action": "topology"}
        self.topoClt = topologyClient()

    def test_TOPO_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.topoClt.topology(self.cookie).body
        self.topoClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

        # self.topoClt.valid_schema_topo_common(resBody)
        # self.topoClt.valid_schema_resul(resBody, schema=scTmp.schema_topology_result)
        # self.topoClt.valid_schema_client(resBody, schema=scTmp.schema_topology_clientInfo)