import time
import pytest
from APIObject.serviceAPI import portforwardViewClient

@pytest.mark.usefixtures("login")
class Test_portView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code":0 , "msg": "Success", "action": "portforwardView"}
        self.portViewClt = portforwardViewClient()

    @pytest.mark.success
    def test_portView_RES_1(self):
        time.sleep(self.timeOut)
        resBody = self.portViewClt.portforwardView(self.cookie).body
        self.portViewClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

