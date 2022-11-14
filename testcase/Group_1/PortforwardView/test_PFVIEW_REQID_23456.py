import time
import pytest
from APIObject.serviceAPI import portforwardViewClient

@pytest.mark.usefixtures("login")
class Test_portView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.data = ['', -3, 3.12, 2147483648, 'abc']
        self.portViewClt = portforwardViewClient()

    def test_portView_ACT_23456(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.portViewClt.Create_portforwardView_Pload(reqID=item)
            resBody = self.portViewClt.portforwardView(self.cookie, pload).body
            resBody_lst.append(resBody)
        self.portViewClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])


