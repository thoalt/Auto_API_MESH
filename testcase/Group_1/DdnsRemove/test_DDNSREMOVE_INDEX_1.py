import time
import pytest
from APIObject.serviceAPI import ddnsRemoveClient, ddnsCreateEditClient


@pytest.mark.usefixtures("login")
class Test_DdnsRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsRemove"}
        self.data = [3, 2, 1, 0]

        self.ddnsRemoveClt = ddnsRemoveClient()
        self.ddnsCreateClt = ddnsCreateEditClient()
        for idx in [0, 1, 2, 3]:
            pload = self.ddnsCreateClt.Create_ddnsCreate_pload(index=idx,
                                                               serviceProvider="ddndns.org.com",
                                                               hostname="abc.com.vn",
                                                               username="user_" + str(idx),
                                                               password="user_" + str(idx))
            resBody = self.ddnsCreateClt.ddnsCreate(self.cookie, pload).body
            time.sleep(15)

    def test_DDNSREMOVE_INDEX_1(self):
        resBody_lst = []
        for item in self.data:
            pload = self.ddnsRemoveClt.Create_ddnsRemove_Pload(index=item)
            resBody = self.ddnsRemoveClt.ddnsRemove(self.cookie, pload).body
            resBody_lst.append(resBody)
            time.sleep(self.timeOut)

        self.ddnsRemoveClt.assert_response_list(resBody_lst,
                                     self.exp['code'],
                                     self.exp['msg'])

