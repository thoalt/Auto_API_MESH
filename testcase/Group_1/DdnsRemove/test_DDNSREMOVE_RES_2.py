import time
import pytest
from APIObject.serviceAPI import ddnsRemoveClient, ddnsCreateEditClient


@pytest.mark.usefixtures("login")
class Test_ddnsView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 590
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsRemove"}
        self.ddnsRemoveClt = ddnsRemoveClient()
        self.idx = 0

        self.ddnsCreateClt = ddnsCreateEditClient()
        pload = self.ddnsCreateClt.Create_ddnsCreate_pload(index=self.idx,
                                                           serviceProvider="ddndns.org.com",
                                                           hostname="abc.com.vn",
                                                           username="user_1",
                                                           password="pass_1")
        resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload).body
        time.sleep(15)

    def test_DDNSVIEW_RES_1(self):
          time.sleep(self.timeOut)
          pload = self.ddnsRemoveClt.Create_ddnsRemove_Pload(index=self.idx)
          resBody = self.ddnsRemoveClt.ddnsRemove(pload=pload, cookies=self.cookie).body
          self.ddnsRemoveClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
