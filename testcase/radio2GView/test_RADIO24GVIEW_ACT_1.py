import time
import pytest
from APIObject.radio24GView import radio24GViewClient

@pytest.mark.usefixtures("login")
class Test_radio24GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 0, "msg": "Success", "action": "radio2.4GView"}
        self.radio24GViewClt = radio24GViewClient()


    @pytest.mark.success
    def test_RADIO24GVIEW_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.radio24GViewClt.radio24GView(self.cookie).body
        self.radio24GViewClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])