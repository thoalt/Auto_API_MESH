import time
import pytest
from APIObject.lanAPI import LanViewClient

@pytest.mark.usefixtures("login")
class Test_LanView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ['lanview1','lanvie']

        self.LanviewClt = LanViewClient()

    def test_LANVIEW_ACT_2(self):
        time.sleep(self.timeOut)
        resbody_Lst = []
        for item in self.data:
            pload = self.LanviewClt.Create_LanView_Pload(action=item)
            resBody = self.LanviewClt.lanView(cookies=self.cookie, pload=pload).body
            resbody_Lst.append(resBody)

        self.LanviewClt.assert_response_list(resbody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])