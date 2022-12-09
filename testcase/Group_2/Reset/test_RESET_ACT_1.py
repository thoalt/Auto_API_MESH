import time
import pytest
from APIObject.reset import resetClient
from Config import config as cfg

@pytest.mark.usefixtures("login")
class Test_Reset():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "reset"}
        self.resetClt = resetClient()
        self.mac = cfg.CAP_MAC

    @pytest.mark.skip(reason="This is Manual Testcase")
    def test_RESET_ACT_1(self):
        time.sleep(self.timeOut)
        pload = self.resetClt.Create_reset_Pload(macList=self.mac)
        resBody = self.resetClt.reset(self.cookie, pload=pload).body

        self.resetClt.assert_response(resBody,
                                      self.exp['code'],
                                      self.exp['msg'],
                                      self.exp['action'])

        time.sleep(240)
