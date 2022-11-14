import time
import pytest
from APIObject.serviceAPI import ddnsRemoveClient

@pytest.mark.usefixtures("login")
class Test_ddnsView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsRemove"}
        self.ddnsRemoveClt = ddnsRemoveClient()
        self.idx = 0

    @pytest.mark.success
    def test_DDNSVIEW_RES_1(self):
          time.sleep(self.timeOut)
          pload = self.ddnsRemoveClt.Create_ddnsRemove_Pload(index=self.idx)
          resBody = self.ddnsRemoveClt.ddnsRemove(pload=pload, cookies=self.cookie).body
          self.ddnsRemoveClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
