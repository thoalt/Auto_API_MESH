import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient

@pytest.mark.usefixtures("login")
class Test_ddnsCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code":0 , "msg": "Success"}
        self.ddnsCreateClt = ddnsCreateEditClient()
        self.idx = 1
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"

    @pytest.mark.success
    def test_ddnsCreate_RES_1(self):
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

