import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient

@pytest.mark.usefixtures("login")
class Test_ddnsView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsCreate"}

        self.ddnsCreateClt = ddnsCreateEditClient()
        self.idx = 3
        self.serProvider = "dyndns.org"
        self.hostname = "test123.com.vn"
        self.username = "thoalt123"
        self.passW = "thoa1234567"

    def test_DDNSVIEW_ACT_1(self):
        time.sleep(self.timeOut)
        pload = self.ddnsCreateClt.Create_ddnsCreate_pload(index=self.idx,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=self.username,
                                                           password=self.passW)

        resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload=pload).body
        self.ddnsCreateClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
