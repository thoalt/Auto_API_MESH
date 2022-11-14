import time
import pytest
from APIObject.reset import resetClient
from Config import config as cfg

@pytest.mark.usefixtures("login")
class Test_Reset():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.resetClt = resetClient()
        self.mac = cfg.CAP_MAC
        self.data = ['', -1, 1.12, 2147483648, 'abc']

        # self.data = [-1]

    @pytest.mark.success
    def test_RESET_ACT_1(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.resetClt.Create_reset_Pload(reqID=item, macList=self.mac)
            resBody = self.resetClt.reset(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
        self.resetClt.assert_response_list(resBody_Lst,
                                          self.exp['code'],
                                          self.exp['msg'])
