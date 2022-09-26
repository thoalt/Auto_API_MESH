import time
import pytest
from APIObject.ping import PingClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.pingClt = PingClient()

    def test_Topology_Schema(self):
        time.sleep(self.timeOut)
        pload = self.pingClt.Create_Ping_Pload(host="8.8.8.8")
        resBody = self.pingClt.ping(self.cookie, pload=pload).body

        self.pingClt.valid_schema_common(resBody)
        self.pingClt.valid_schema_resul(resBody, schema=scTmp.schema_ping_result)

