import time
import pytest
from APIObject.wanAPI import WanRemoveClient

@pytest.mark.usefixtures("login")
class Test_Wanview():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.wanRemoveClt = WanRemoveClient()
        self.wanIdx = [0, 4, "1", "2", "3", -1, 1.12, '', 'abc']


    def test_WAN_REMOVE_RES_1(self):
        resBody_Lst = []
        for item in self.wanIdx:
            pload = self.wanRemoveClt.Create_WanRemove_Pload(wanIndex=item)
            resBody = self.wanRemoveClt.wanRemove(self.cookie, pload=pload).body
            time.sleep(self.timeOut)
            resBody_Lst.append(resBody)
        self.wanRemoveClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])


