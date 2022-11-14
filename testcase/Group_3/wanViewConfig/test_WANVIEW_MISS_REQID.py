import time
import pytest
from APIObject.wanAPI import WanViewConfigClient

@pytest.mark.usefixtures("login")
class Test_Wanview():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 9, "msg": "Miss Request ID"}
        self.WanviewClt = WanViewConfigClient()
        pload = self.WanviewClt.Create_WanViewConfig_Pload()
        self.data = [self.WanviewClt.Remove_Key_In_Pload(pload, 'requestId')]


    def test_WANVIEW_ACT_2(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            resBody = self.WanviewClt.wanViewConfig(self.cookie, pload=item).body
            resBody_Lst.append(resBody)
        self.WanviewClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
