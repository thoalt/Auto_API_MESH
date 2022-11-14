import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient


@pytest.mark.usefixtures("login")
class Test_DdnsCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsCreate"}
        self.data = [0,1,2,3]

        self.ddnsCreateClt = ddnsCreateEditClient()
        #self.idx = 1
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"

    def test_DDNSCREATE_INDEX_1(self):
        resBody_lst = []
        for item in self.data:
            pload = self.ddnsCreateClt.Create_ddnsCreate_pload(index=item,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=self.username,
                                                           password=self.passW)
            resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload).body
            resBody_lst.append(resBody)
            time.sleep(self.timeOut)


        self.ddnsCreateClt.assert_response_list(resBody_lst,
                                     self.exp['code'],
                                     self.exp['msg'])

