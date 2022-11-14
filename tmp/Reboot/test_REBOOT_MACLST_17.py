import time
import pytest
from APIObject.reboot import rebootClient
import Config.config as cfg

@pytest.mark.usefixtures("login")
class Test_Reboot():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.rebootClt = rebootClient()
        self.mac = cfg.CAP_MAC
        self.data = [cfg.CAP_MAC + ";" + cfg.MRE1_MAC]

    def test_REBOOT_ACT_2(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.rebootClt.Create_Reboot_Pload(macList=item)
            resBody = self.rebootClt.reboot(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)

        self.rebootClt.assert_response_list(resBody_Lst,
                                    self.exp['code'],
                                    self.exp['msg'])

