import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient

@pytest.mark.usefixtures("login")
class Test_ddnsCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsCreate"}
        self.data = [2147483647]
        #1, 2147483646, 2147483647
        self.ddnsCreateClt = ddnsCreateEditClient()
        self.idx = 2
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"


    def test_DDNSCREATE_REQID_1(self):
        resBody_Lst = []
        for item in self.data:
            pload = self.ddnsCreateClt.Create_ddnsCreate_pload(reqID=item, index=self.idx,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=self.username,
                                                           password=self.passW)
            resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
            time.sleep(self.timeOut)
            
        self.ddnsCreateClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
