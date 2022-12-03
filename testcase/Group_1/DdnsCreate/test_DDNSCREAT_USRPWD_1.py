import time
import pytest
from APIObject.serviceAPI import ddnsCreateEditClient, ddnsRemoveClient


@pytest.mark.usefixtures("login")
class Test_DdnsCreate():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsCreate"}
        self.ddnsRevClt = ddnsRemoveClient()


        # self.data = ["uidwvgNleD1234567890`~!@#$%^*()_dkfhgidfhifghfjhjhdf784u685735jkydfjhus6743!@#$@%[];gfggdsghdhghdjhfdhghgdsfhdhgdhfgh425435267!@"]
        self.data = ["quan", "QUAN", "1quan", "1QUAN", "123", "a", "5", "%", "q!",
        "uidwvgNleD1234567890`~!@#$%^*()_dkfhgidfhifghfjhjhdf784u685735jkydfjhus6743!@#$@%[];gfggdsghdhghdjhfdhghgdsfhdhgdhfgh425435267!@"]

        self.ddnsCreateClt = ddnsCreateEditClient()
        self.idx = 1
        self.serProvider = "dyndns.org"
        self.hostname = "test.com.vn"
        #self.username = "thoalt"
        self.passW = "thoa12345"

    def test_DDNSCREATE_USRPWD_1(self):
        resBody_lst = []
        for item in self.data:
            self.ddnsRevClt.ddns_remove_all(self.cookie)

            pload = self.ddnsCreateClt.Create_ddnsCreate_pload(index=self.idx,
                                                           serviceProvider=self.serProvider,
                                                           hostname=self.hostname,
                                                           username=item,
                                                           password=item)
            resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload).body
            resBody_lst.append(resBody)
            time.sleep(self.timeOut)

        self.ddnsCreateClt.assert_response_list(resBody_lst,
                                         self.exp['code'],
                                         self.exp['msg'])


