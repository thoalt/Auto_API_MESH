import time
import pytest
from APIObject.topology import topologyClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.topoClt = topologyClient()

    def test_Topology_Schema(self):
        time.sleep(self.timeOut)
        resBody = self.topoClt.topology(self.cookie).body

        self.topoClt.valid_schema_topo_common(resBody)
        self.topoClt.valid_schema_resul(resBody, schema=scTmp.schema_topology_result)
        self.topoClt.valid_schema_client(resBody, schema=scTmp.schema_topology_clientInfo)

