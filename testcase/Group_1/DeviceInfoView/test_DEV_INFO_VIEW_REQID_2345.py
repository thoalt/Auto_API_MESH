import time
import pytest
from APIObject.deviceInfoView import deviceInfoViewClient

@pytest.mark.usefixtures("login")
class Test_TraceRoute():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.data = ['', -1, 1.12, 2147483648, 'abc']
        self.devInf = deviceInfoViewClient()


    def test_TRACE_ROUTE_RES_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.devInf.Create_deviceInfoView_Pload(reqID=item)
            resBody = self.devInf.deviceInfoView(cookies=self.cookie, pload=pload).body
            resBody_lst.append(resBody)
        self.devInf.assert_response_list(resBody_lst,
                                           self.exp['code'],
                                           self.exp['msg'])


