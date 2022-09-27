import time
import pytest
from APIObject.wanAPI import WanViewConfigClient

@pytest.mark.usefixtures("login")
class Test_Wanview():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 0, "msg": "Success", "action": "wanViewConfig"}
        self.data = [0, 1, 2147483646, 2147483647]
        self.WanviewClt = WanViewConfigClient()

    @pytest.mark.success
    def test_WANVIEW_REQID_1(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.WanviewClt.Create_WanView_Pload(reqID=item)
            resBody = self.WanviewClt.wanViewConfig(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
        self.WanviewClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

