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
        self.mac = cfg.CAP_MAC + "," + cfg.MRE1_MAC
        self.fwName = "EW12_EW12ST000T1002.tar.gz"
        self.md5 = "5ddf18c098b5e5fd811b7d3ede63fdb7"

    @pytest.mark.skip(reason="This is Manual Testcase")
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


