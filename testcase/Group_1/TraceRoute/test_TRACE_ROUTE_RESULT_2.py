import time
import pytest
from APIObject.traceroute import TracerouteClient

@pytest.mark.usefixtures("login")
class Test_TraceRoute():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code":0, "msg": "Success", "action":"traceroute", "traceCode": 3}
        self.host = "8.8.8.8"
        self.traceClt = TracerouteClient()


    def test_TRACE_ROUTE_RES_1(self):
        time.sleep(self.timeOut)
        pload = self.traceClt.Create_TraceRoute_Pload(host=self.host)
        resBody = self.traceClt.traceroute(cookies=self.cookie, pload=pload).body
        self.traceClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])
        self.traceClt.assert_trace_result(resBody, traceCode=self.exp['traceCode'])


