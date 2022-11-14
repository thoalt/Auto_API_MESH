import time
import pytest
from APIObject.logout import LogoutClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.Logout = LogoutClient()

    def test_Topology_Schema(self):
        time.sleep(self.timeOut)
        resBody = self.Logout.logout(self.cookie).body

        self.Logout.valid_schema_topo_common(resBody, schema=scTmp.schema_dataNull_common)


