import time
import pytest
from APIObject.serviceAPI import portforwardRemoveClient

@pytest.mark.usefixtures("login")
class Test_portRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.portRemoveClt = portforwardRemoveClient()
        self.idx = 2
        self.data = ["“", "‘", "|", "/", "\\", ",", ";", ":", "&", "<", ">", "^", "*", "?", "ă", "â", "đ",
                     "ê", "ô", "ơ", "ư", "á", "à", "ạ", "ả", "ã",
                    "Ă", "Â", "Đ", "Ê", "Ô", "Ơ", "Ư", "Á", "À", "Ạ", "Ả", "Ã",
                     'portforward Remove', 'portforwardRemove ', '  portforwardRemove']

    def test_portRemove_ACT_678(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
           pload = self.portRemoveClt.Create_portforwardRemove_Pload(ruleIndex=self.idx, action=item)
           resBody = self.portRemoveClt.portforwardRemove(self.cookie, pload=pload).body
           resBody_lst.append(resBody)
        self.portRemoveClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])

