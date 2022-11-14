import time
import pytest
from APIObject.lanAPI import LanViewClient

@pytest.mark.usefixtures("login")
class Test_LanView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 610
        self.exp = {"code": 15, "msg": "Session Timeout"}
        self.LanviewClt = LanViewClient()

    def test_LANVIEW_RES_3(self):
        time.sleep(self.timeOut)
        response = self.LanviewClt.lanView(self.cookie)
        resBody = response.body
        self.LanviewClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],)