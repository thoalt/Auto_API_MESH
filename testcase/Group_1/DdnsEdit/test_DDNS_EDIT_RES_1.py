import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient

@pytest.mark.usefixtures("login")
class Test_ddnsCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code":0 , "msg": "Success"}
        self.ddnsEditClt = ddnsCreateEditClient()
        self.idx = 1
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"


    def test_ddnsCreate_RES_1(self):
        time.sleep(self.timeOut)
        pload = self.ddnsEditClt.Create_ddnsEdit_Pload(index=self.idx,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=self.username,
                                                           password=self.passW)

        resBody = self.ddnsEditClt.ddnsCreate(self.cookie, pload=pload).body
        self.ddnsEditClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])

