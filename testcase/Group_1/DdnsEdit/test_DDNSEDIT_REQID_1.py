import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient

@pytest.mark.usefixtures("login")
class Test_ddnsView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 15
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsEdit"}
        self.data = [0, 1, 2147483646, 2147483647]
        self.ddnsEditClt = ddnsCreateEditClient()
        self.idx = 0
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"

        self.ddnsRevClt = ddnsRemoveClient()
        self.ddnsRevClt.ddns_remove_all(self.cookie)

        self.ddnsCreateClt = ddnsCreateEditClient()
        pload = self.ddnsCreateClt.Create_ddnsCreate_pload(index=self.idx,
                                                           serviceProvider="ddndns.org.com",
                                                           hostname="abc.com.vn",
                                                           username="user_1",
                                                           password="pass_1")
        resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload).body
        time.sleep(15)
    def test_DDNSEDIT_REQID_1(self):
        resBody_Lst = []
        for idx, item in enumerate(self.data):
            pload = self.ddnsEditClt.Create_ddnsEdit_Pload(reqID=item, index=idx,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=self.username,
                                                           password=self.passW)
            resBody = self.ddnsEditClt.ddnsEdit(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
            time.sleep(self.timeOut)
            
        self.ddnsEditClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])


