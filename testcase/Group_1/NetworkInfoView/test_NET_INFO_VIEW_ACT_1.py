import time
import pytest
from APIObject.networkinfoView import networkinfoViewClient


@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "networkinfoView"}
        self.netInf = networkinfoViewClient()



    def test_DEV_INFO_VIEW_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.netInf.networkinfoView(self.cookie).body
        self.netInf.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])