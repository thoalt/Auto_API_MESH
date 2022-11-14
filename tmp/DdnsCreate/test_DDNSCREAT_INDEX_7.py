import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient


@pytest.mark.usefixtures("login")
class Test_DdnsCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 12, "msg": "Unknown Error", "action": "ddnsCreate"}

        self.ddnsCreateClt = ddnsCreateEditClient()
        self.idx = 0
        self.serProvider = "dyndns.org"
        self.serProvider = "changeip.com"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"

    def test_DDNSCREATE_INDEX_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        pload = self.ddnsCreateClt.Create_ddnsCreate_pload(index=self.idx,
                                                       serviceProvider=self.serProvider,
                                                       hostname=self.hostname,
                                                       username=self.username,
                                                       password=self.passW)
        resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload).body

        pload2 = self.ddnsCreateClt.Create_ddnsCreate_pload(index=self.idx,
                                                           serviceProvider=self.serProvider2,
                                                           hostname=self.hostname + 'a',
                                                           username=self.username + 'a',
                                                           password=self.passW + 'a')
        resBody2 = self.ddnsCreateClt.ddnsCreate(self.cookie, pload2).body

        resBody_lst.append(resBody2)


        self.ddnsCreateClt.assert_response_list(resBody_lst,
                                     self.exp['code'],
                                     self.exp['msg'])

