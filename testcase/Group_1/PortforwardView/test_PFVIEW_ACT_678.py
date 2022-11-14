import time
import pytest
from APIObject.serviceAPI import portforwardViewClient

@pytest.mark.usefixtures("login")
class Test_portView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.portViewClt = portforwardViewClient()
        self.data = ["“", "‘", "|", "/", "\\", ",", ";", ":", "&", "<", ">", "^", "*", "?", "ă", "â",
                     "đ", "ê", "ô", "ơ", "ư", "á", "à", "ạ", "ả", "ã",
                    "Ă", "Â", "Đ", "Ê", "Ô", "Ơ", "Ư", "Á", "À", "Ạ", "Ả", "Ã", "portforward View", " portforwardView", "portforwardView  "]

    def test_portView_ACT_678(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.portViewClt.Create_portforwardView_Pload(action=item)
            resBody = self.portViewClt.portforwardView(self.cookie, pload).body
            resBody_lst.append(resBody)
        self.portViewClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])


