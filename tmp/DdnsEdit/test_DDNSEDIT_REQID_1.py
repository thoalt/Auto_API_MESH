import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient

@pytest.mark.usefixtures("login")
class Test_ddnsView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsEdit"}
        self.data = [0, 1, 2147483646, 2147483647]
        self.ddnsEditClt = ddnsCreateEditClient()
        self.idx = 0
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"

    @pytest.mark.success
    def test_DDNSEDIT_REQID_1(self):
        resBody_Lst = []
        for item in self.data:
            pload = self.ddnsEditClt.Create_ddnsEdit_Pload(reqID=item, index=self.idx,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=self.username,
                                                           password=self.passW)
            resBody = self.ddnsEditClt.ddnsEdit(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
            time.sleep(self.timeOut)
            
        self.ddnsEditClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

