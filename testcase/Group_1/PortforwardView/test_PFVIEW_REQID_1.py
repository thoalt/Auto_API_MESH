import time
import pytest
from APIObject.serviceAPI import portforwardViewClient

@pytest.mark.usefixtures("login")
class Test_portView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success"}
        self.data = [0, 1, 2147483646, 2147483647]
        self.portViewClt = portforwardViewClient()

    def test_portView_ACT_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.portViewClt.Create_portforwardView_Pload(reqID=item)
            resBody = self.portViewClt.portforwardView(self.cookie, pload).body
            resBody_lst.append(resBody)
        self.portViewClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])


