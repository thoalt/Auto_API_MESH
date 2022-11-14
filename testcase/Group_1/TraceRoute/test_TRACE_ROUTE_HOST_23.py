import time
import pytest
from APIObject.traceroute import TracerouteClient

@pytest.mark.usefixtures("login")
class Test_TraceRoute():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.host = "8.8.8.8"
        self.data = ["8.8.8.", "8.8", "8", "8.8.8.8.8"]
        # self.data = ["8.8.8.", "8.8.8.8.8"]

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
                                            self.exp['msg'])

