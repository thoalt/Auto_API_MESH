import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient


@pytest.mark.usefixtures("login")
class Test_DdnsCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail", "action": "ddnsCreate"}
        self.data = ["dyndns1.org", "1changeip.com", "quan.abc", "google.com"]

        self.ddnsCreateClt = ddnsCreateEditClient()
        self.idx = 0
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"

    def test_DDNSEDIT_PROVIDER_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.ddnsCreateClt.Create_ddnsCreate_pload(index=self.idx,
                                                           serviceProvider=item,
                                                           hostname=self.hostname,
                                                           username=self.username,
                                                           password=self.passW)
            resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload).body
            resBody_lst.append(resBody)

        self.ddnsCreateClt.assert_response_list(resBody_lst,
                                         self.exp['code'],
                                         self.exp['msg'])


