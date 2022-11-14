import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient

@pytest.mark.usefixtures("login")
class Test_ddnsView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ['openSession122144124141241241241']
        self.ddnsCreateClt = ddnsCreateEditClient()
        self.idx = 0
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"

    @pytest.mark.success
    def test_DDNSVIEW_ACT_5(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.ddnsCreateClt.Create_ddnsCreate_pload(action=item, index=self.idx,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=self.username,
                                                           password=self.passW)
            resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
        self.ddnsCreateClt.assert_response_list(resBody_Lst,
                                              self.exp['code'],
                                              self.exp['msg'])