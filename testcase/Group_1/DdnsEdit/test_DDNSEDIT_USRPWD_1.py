import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient, ddnsRemoveClient


@pytest.mark.usefixtures("login")
class Test_ddnsEdit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 15
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsEdit"}
        self.data = ["123", "a", "5", "%", "q!",
                    "uidwvgNleD1234567890`~!@#$%^*()_dkfhgidfhifghfjhjhdf784u685735jkydfjhus6743!@#$@%[];gfggdsghdhghdjhfdhghgdsfhdhgdhfgh425435267!@"]

        self.ddnsEditClt = ddnsCreateEditClient()
        self.idx = 0
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"

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

    def test_DDNSEDIT_USRPWD_1(self):
        resBody_lst = []
        for idx, item in enumerate(self.data):
            pload = self.ddnsEditClt.Create_ddnsEdit_Pload(index=idx,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=item,
                                                           password=item)
            resBody = self.ddnsEditClt.ddnsEdit(self.cookie, pload).body
            resBody_lst.append(resBody)
            time.sleep(self.timeOut)

        self.ddnsEditClt.assert_response_list(resBody_lst,
                                         self.exp['code'],
                                         self.exp['msg'])


