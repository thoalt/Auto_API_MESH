import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient

@pytest.mark.usefixtures("login")
class Test_ddnsView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 590
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsEdit"}
        self.ddnsEditClt = ddnsCreateEditClient()

    @pytest.mark.success
    def test_DDNSVIEW_RES_1(self):
          time.sleep(self.timeOut)
          resBody = self.ddnsEditClt.ddnsEdit(self.cookie).body
          self.ddnsEditClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
