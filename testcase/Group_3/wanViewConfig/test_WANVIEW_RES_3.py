import time
import pytest
from APIObject.wanAPI import WanViewConfigClient

@pytest.mark.usefixtures("login")
class Test_Wanview():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 610
        self.exp = {"code": 15, "msg": "Session Timeout"}
        self.WanviewClt = WanViewConfigClient()


    def test_WANVIEW_RES_1(self):
        time.sleep(self.timeOut)
        resBody = self.WanviewClt.wanViewConfig(self.cookie).body
        self.WanviewClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])


