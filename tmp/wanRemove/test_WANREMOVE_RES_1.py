import time
import pytest
from APIObject.wanAPI import WanRemoveClient

@pytest.mark.usefixtures("login")
class Test_Wanview():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code":0, "msg": "Success", "action":"wanRemove"}
        self.wanRemoveClt = WanRemoveClient()
        self.wanIdx = 2

    @pytest.mark.success
    def test_WAN_REMOVE_RES_1(self):
        time.sleep(self.timeOut)
        pload = self.wanRemoveClt.Create_WanRemove_Pload(wanIndex=self.wanIdx)
        resBody = self.wanRemoveClt.wanRemove(self.cookie, pload=pload).body
        self.wanRemoveClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])


