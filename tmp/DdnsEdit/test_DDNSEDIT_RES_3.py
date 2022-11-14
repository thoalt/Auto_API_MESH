import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient

@pytest.mark.usefixtures("login")
class Test_ddnsEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 610
        self.exp = {"code": 15, "msg": "Session Timeout", "action": "ddnsEdit"}
        self.ddnsEditClt = ddnsCreateEditClient()

    @pytest.mark.success
    def test_DDNSEDIT_RES_1(self):
          time.sleep(self.timeOut)
          resBody = self.ddnsEditClt.ddnsEdit(self.cookie).body
          self.ddnsEditClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
