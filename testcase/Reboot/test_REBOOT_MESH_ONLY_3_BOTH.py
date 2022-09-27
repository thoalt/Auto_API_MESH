import time
import pytest
from APIObject.reboot import rebootClient
import Config.config as cfg


@pytest.mark.usefixtures("login")
class Test_Reboot():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "reboot"}
        self.rebootClt = rebootClient()
        self.data = cfg.CAP_MAC + "," + cfg.MRE1_MAC



    @pytest.mark.success
    def test_REBOOT_ACT_1(self):
        time.sleep(self.timeOut)
        pload = self.rebootClt.Create_Reboot_Pload(macList=self.data)
        resBody = self.rebootClt.reboot(self.cookie, pload=pload).body

        self.rebootClt.assert_response(resBody,
                                    self.exp['code'],
                                    self.exp['msg'],
                                    self.exp['action'])
