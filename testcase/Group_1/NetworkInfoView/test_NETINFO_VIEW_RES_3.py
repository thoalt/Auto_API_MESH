import time
import pytest
from APIObject.networkinfoView import networkinfoViewClient


@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 610
        self.exp = {"code": 15, "msg": "Session Timeout"}
        self.netInf = networkinfoViewClient()



    def test_NETINFO_VIEW_RES_3(self):
        time.sleep(self.timeOut)
        resBody = self.netInf.networkinfoView(self.cookie).body
        self.netInf.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])