import time
import pytest
from APIObject.wanViewConfig import WanViewClient


@pytest.mark.usefixtures("login")
class Test_Wanview():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.host = "8.8.8.8"
        self.data = ['wanViewConfig1']

        self.WanviewClt = WanViewClient()


    @pytest.mark.success
    def test_WANVIEW_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.WanviewClt.wanViewConfig(self.cookie).body
        self.WanviewClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])