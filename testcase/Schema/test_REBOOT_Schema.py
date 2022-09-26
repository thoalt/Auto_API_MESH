import time
import pytest
from APIObject.reboot import rebootClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_Reboot():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.rebootClt = rebootClient()
        self.data = "A4:F4:C2:0B:44:68, A4:F4:C2:0B:44:54"

    def test_Topology_Schema(self):
        time.sleep(self.timeOut)
        pload = self.rebootClt.Create_Reboot_Pload(macList=self.data)
        resBody = self.rebootClt.reboot(self.cookie, pload=pload).body

        self.rebootClt.valid_schema_common(resBody)
        self.rebootClt.valid_schema_resul(resBody, schema=scTmp.schema_reboot_result)


