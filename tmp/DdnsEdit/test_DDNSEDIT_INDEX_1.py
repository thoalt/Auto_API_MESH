import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient


@pytest.mark.usefixtures("login")
class Test_DdnsEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsEdit"}
        self.data = [0, 1, 2, 3]

        self.ddnsEditClt = ddnsCreateEditClient()
        self.idx = 0
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        self.username = "thoalt"
        self.passW = "thoa12345"

    def test_DDNSEDIT_INDEX_1(self):
        resBody_lst = []
        for item in self.data:
            pload = self.ddnsEditClt.Create_ddnsEdit_Pload(index=item,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=self.username,
                                                           password=self.passW)
            resBody = self.ddnsEditClt.ddnsEdit(self.cookie, pload).body
            resBody_lst.append(resBody)
            time.sleep(self.timeOut)

        self.ddnsEditClt.assert_response_list(resBody_lst,
                                     self.exp['code'],
                                     self.exp['msg'])

