import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient


@pytest.mark.usefixtures("login")
class Test_DdnsEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail", "action": "ddnsCreat"}
        self.data = ['']

        self.ddnsEditClt = ddnsCreateEditClient()
        self.idx = 0
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"

    def test_DDNSEDIT_USRPWD_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.ddnsEditClt.Create_ddnsEdit_Pload(index=self.idx,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=item,
                                                           password=item)
            resBody = self.ddnsEditClt.ddnsEdit(self.cookie, pload).body
            resBody_lst.append(resBody)

        self.ddnsEditClt.assert_response_list(resBody_lst,
                                         self.exp['code'],
                                         self.exp['msg'])


