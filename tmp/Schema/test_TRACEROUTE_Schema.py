import time
import pytest
from APIObject.traceroute import TracerouteClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_TraceRoute():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.traceClt = TracerouteClient()

    def test_TraceRoute_Schema(self):
        time.sleep(self.timeOut)
        pload = self.traceClt.Create_TraceRoute_Pload(host="8.8.8.8")
        resBody = self.traceClt.traceroute(self.cookie, pload=pload).body

        self.traceClt.valid_schema_common(resBody, schema=scTmp.schema_traceroute_common)
        self.traceClt.valid_schema_resul(resBody, schema=scTmp.schema_traceroute_result)
