import time
import pytest
from APIObject.serviceAPI import ddnsViewClient

@pytest.mark.usefixtures("login")
class Test_ddnsView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ['']
        self.ddnsViewClt = ddnsViewClient()



    def test_DDNSVIEW_ACT_4(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.ddnsViewClt.Create_ddnsView_Pload(action=item)
            resBody = self.ddnsViewClt.ddnsView(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
        self.ddnsViewClt.assert_response_list(resBody_Lst,
                                              self.exp['code'],
                                              self.exp['msg'])