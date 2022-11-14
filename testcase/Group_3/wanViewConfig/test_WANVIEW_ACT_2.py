import time
import pytest
from APIObject.wanAPI import WanViewConfigClient

@pytest.mark.usefixtures("login")
class Test_Wanview():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ['wanviewconfig1','wanviewconfi']
        self.WanviewClt = WanViewConfigClient()



    def test_WANVIEW_ACT_2(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.WanviewClt.Create_WanViewConfig_Pload(action=item)
            resBody = self.WanviewClt.wanViewConfig(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
        self.WanviewClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
