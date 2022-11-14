import time
import pytest
from APIObject.traceroute import TracerouteClient

@pytest.mark.usefixtures("login")
class Test_TraceRoute():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 9, "msg": "Miss Request ID"}
        self.host = "8.8.8.8"
        self.traceClt = TracerouteClient()
        pload = self.traceClt.Create_TraceRoute_Pload(host=self.host)
        self.data = [self.traceClt.Remove_Key_In_Pload(pload, 'requestId')]


    def test_TRACE_ROUTE_RES_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            resBody = self.traceClt.traceroute(cookies=self.cookie, pload=item).body
            resBody_lst.append(resBody)
        self.traceClt.assert_response_list(resBody_lst,
                                            self.exp['code'],
                                            self.exp['msg'])


