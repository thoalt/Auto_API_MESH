import time
import pytest
from APIObject.serviceAPI import portforwardViewClient

@pytest.mark.usefixtures("login")
class Test_portView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 9, "msg": "Miss Request ID"}
        self.portViewClt = portforwardViewClient()
        pload = self.portViewClt.Create_portforwardView_Pload()
        self.data = self.portViewClt.Remove_Request_ID_In_Pload(pload)

    def test_portView_miss_ATTB(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            resBody = self.portViewClt.portforwardView(self.cookie, pload=item).body
            resBody_lst.append(resBody)
        self.portViewClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])


