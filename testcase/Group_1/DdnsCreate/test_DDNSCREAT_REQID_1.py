import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient, ddnsRemoveClient


@pytest.mark.usefixtures("login")
class Test_ddnsCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsCreate"}
        self.data = [1, 2,  2147483646, 2147483647]
        self.ddnsRevClt = ddnsRemoveClient()
        self.ddnsRevClt.ddns_remove_all(self.cookie)

        self.ddnsCreateClt = ddnsCreateEditClient()
        self.idx = 0
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"


    def test_DDNSCREATE_REQID_1(self):
        resBody_Lst = []
        for idx, item in enumerate(self.data):
            pload = self.ddnsCreateClt.Create_ddnsCreate_pload(reqID=item,
                                                           index=idx,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=self.username + str(idx),
                                                           password=self.passW + str(idx))
            resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
            time.sleep(30)
            
        self.ddnsCreateClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
