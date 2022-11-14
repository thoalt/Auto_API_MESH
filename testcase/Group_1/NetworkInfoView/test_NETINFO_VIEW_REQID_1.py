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
        self.data = [0, 1, 2147483646, 2147483647]



    def test_NETINFO_VIEW_REQID_1(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.netInf.Create_networkinfoView_Pload(reqID=item)
            resBody = self.netInf.networkinfoView(self.cookie,pload=pload).body
            resBody_Lst.append(resBody)
        self.netInf.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
