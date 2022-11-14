import time
import pytest
from APIObject.wanAPI import WanViewStatusClient

@pytest.mark.usefixtures("login")
class Test_Wanview():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code":0, "msg": "Success", "action":"wanViewStatus"}
        self.wanStaClt = WanViewStatusClient()

    @pytest.mark.success
    def test_WANVIEW_RES_1(self):
        time.sleep(self.timeOut)
        resBody = self.wanStaClt.wanViewStatus(self.cookie).body
        self.wanStaClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])


