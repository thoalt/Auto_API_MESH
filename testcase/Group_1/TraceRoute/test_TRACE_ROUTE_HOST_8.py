import time
import pytest
from APIObject.traceroute import TracerouteClient

@pytest.mark.usefixtures("login")
class Test_TraceRoute():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.data = ["ă", "â", "đ", "ê", "ô", "ơ", "ư", "á", "à", "ạ", "ả", "ã",
                     "Ă", "Â", "Đ", "Ê", "Ô", "Ơ", "Ư", "Á", "À", "Ạ", "Ả", "Ã"]

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

