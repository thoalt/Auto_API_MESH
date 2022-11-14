import time
import pytest
from APIObject.networkinfoView import networkinfoViewClient


@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 11, "msg": "Verify Fail", "action": "networkinfoView"}
        self.netInf = networkinfoViewClient()
        self.data = [-1, 1.12, 2147483648, 'abc' ]



    def test_NETINFO_VIEW_REQID_2(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.netInf.Create_networkinfoView_Pload(reqID=item)
            resBody = self.netInf.networkinfoView(self.cookie,pload=pload).body
            resBody_Lst.append(resBody)
        self.netInf.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
