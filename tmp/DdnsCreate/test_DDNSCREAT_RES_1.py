import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient

@pytest.mark.usefixtures("login")
class Test_ddnsCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsEdit"}
        self.ddnsCreateClt = ddnsCreateEditClient()

    @pytest.mark.success
    def test_DDNSCREATE_RES_1(self):
          time.sleep(self.timeOut)
          resBody = self.ddnsCreateClt.ddnsCreate(self.cookie).body
          self.ddnsCreateClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])