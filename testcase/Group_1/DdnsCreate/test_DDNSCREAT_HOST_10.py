import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient, ddnsRemoveClient


@pytest.mark.usefixtures("login")
class Test_DdnsEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail", "action": "ddnsCreat"}
        self.ddnsRevClt = ddnsRemoveClient()
        self.ddnsRevClt.ddns_remove_all(self.cookie)

        self.ddnsCreateClt = ddnsCreateEditClient()
        self.idx = 0
        self.serProvider = "dyndns.org"
        self.serProvider2 = "changeip.com"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"

    def test_DDNSEDIT_RES_HOST_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        pload = self.ddnsCreateClt.Create_ddnsCreate_pload(index=self.idx,
                                                       serviceProvider=self.serProvider,
                                                       hostname=self.hostname,
                                                       username=self.username,
                                                       password=self.passW)
        resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload).body

        pload2 = self.ddnsCreateClt.Create_ddnsCreate_pload(index=self.idx + 1,
                                                           serviceProvider=self.serProvider2,
                                                           hostname=self.hostname,
                                                           username=self.username + 'a',
                                                           password=self.passW + 'a')
        resBody2 = self.ddnsCreateClt.ddnsCreate(self.cookie, pload2).body

        resBody_lst.append(resBody2)

        self.ddnsCreateClt.assert_response_list(resBody_lst,
                                     self.exp['code'],
                                     self.exp['msg'])

