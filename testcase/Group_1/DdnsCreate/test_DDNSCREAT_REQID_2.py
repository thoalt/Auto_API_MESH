import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient


@pytest.mark.usefixtures("login")
class Test_ddnsCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code":11 , "msg": "Verify Fail"}
        self.data = ['']
        self.ddnsCreateClt = ddnsCreateEditClient()
        self.idx = 0
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"


    def test_DDNSCREATE_REQID_1(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.ddnsCreateClt.Create_ddnsCreate_pload(reqID=item, index=self.idx,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=self.username,
                                                           password=self.passW)
            resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)

        self.ddnsCreateClt.assert_response_list(resBody_Lst,
                                              self.exp['code'],
                                              self.exp['msg'])
