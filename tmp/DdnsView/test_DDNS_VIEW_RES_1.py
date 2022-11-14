import time
import pytest
from APIObject.serviceAPI import ddnsViewClient

@pytest.mark.usefixtures("login")
class Test_portView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 0, "msg": "Success", "action": "ddnsView"}
        self.ddnsViewClt = ddnsViewClient()

    @pytest.mark.success
    def test_portView_RES_1(self):
        time.sleep(self.timeOut)
        resBody = self.ddnsViewClt.ddnsView(self.cookie).body
        self.ddnsViewClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

