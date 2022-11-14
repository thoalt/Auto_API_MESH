import time
import pytest
from APIObject.lanAPI import LanViewClient

@pytest.mark.usefixtures("login")
class Test_LanView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success", "action": "lanView"}
        self.LanviewClt = LanViewClient()


    def test_LANVIEW_RES_1(self):
        time.sleep(self.timeOut)
        response = self.LanviewClt.lanView(self.cookie)
        resBody = response.body
        self.LanviewClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])