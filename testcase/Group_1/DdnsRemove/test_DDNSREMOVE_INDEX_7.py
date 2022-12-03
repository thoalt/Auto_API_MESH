import time
import pytest
from APIObject.serviceAPI import ddnsRemoveClient


@pytest.mark.usefixtures("login")
class Test_DdnsRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.data = [3]

        self.ddnsRemoveClt = ddnsRemoveClient()

    def test_DDNSREMOVE_INDEX_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.ddnsRemoveClt.Create_ddnsRemove_Pload(index=item)
            resBody = self.ddnsRemoveClt.ddnsRemove(self.cookie, pload).body
            resBody_lst.append(resBody)

        self.ddnsRemoveClt.assert_response_list(resBody_lst,
                                     self.exp['code'],
                                     self.exp['msg'])

