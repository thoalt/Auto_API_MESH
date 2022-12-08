import time
import pytest
from APIObject.updateFirmware import UpdateFWClient
import Config.config as cfg

@pytest.mark.usefixtures("login")
class Test_Wan_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success"}
        self.upFWClt = UpdateFWClient()
        self.mac = cfg.MRE1_MAC
        self.fwName = "EW12_EW12ST000U1002.tar.gz"
        self.md5 = "1ad7f4f40ebe8490c7df47ea8fe199e9"

    # @pytest.mark.skip(reason="This is Manual Testcase")
    def test_UPGRADE_FW_MESH_ONLY_1(self):
        time.sleep(self.timeOut)
        pload = self.upFWClt.Create_UpdateFW_Pload(
            macList=self.mac,
            fileName=self.fwName,
            md5sum=self.md5
        )
        resBody = self.upFWClt.UpdateFirmware(self.cookie, pload=pload).body
        time.sleep(240)
        self.upFWClt.assert_response(resBody,
                                       self.exp['code'],
                                       self.exp['msg'])


