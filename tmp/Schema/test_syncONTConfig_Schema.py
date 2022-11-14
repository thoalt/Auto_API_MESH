import time
import pytest
from APIObject.syncONTConfig import syncONTConfigClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.syncONT = syncONTConfigClient()

    def test_Topology_Schema(self):
        time.sleep(self.timeOut)
        resBody = self.syncONT.syncONTConfig(self.cookie).body

        self.syncONT.valid_schema_common(resBody, schema=scTmp.schema_syncONTConfig)

