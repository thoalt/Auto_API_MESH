import time
import pytest
from APIObject.traceroute import TracerouteClient

@pytest.mark.usefixtures("login")
class Test_TraceRoute():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 0, "msg": "Success", "action": "traceroute", "traceCode": 6}
        self.data = [" 8.8.8.8", "8.8 .8.8", "8.8.8.8 ", " google.com.vn", "google. com.vn", "google.com.vn "]
        self.traceClt = TracerouteClient()


    def test_TRACE_ROUTE_RES_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.traceClt.Create_TraceRoute_Pload(host=item)
            resBody = self.traceClt.traceroute(cookies=self.cookie, pload=pload).body
            resBody_lst.append(resBody)
        self.traceClt.assert_response_list(resBody_lst,
                                            self.exp['code'],
                                            self.exp['msg'],
                                            self.exp['action'])
        self.traceClt.assert_trace_result_lst(resBody_lst, traceCode=self.exp['traceCode'])

