import time
import pytest
from APIObject.lanAPI import LanViewClient


@pytest.mark.usefixtures("login")
class Test_LanView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "lanView"}
        self.data = [0, 1, 2147483646, 2147483647]

        self.LanviewClt = LanViewClient()

    def test_LANVIEW_REQID_1(self):
        time.sleep(self.timeOut)
        resbody_Lst = []
        for item in self.data:
            pload = self.LanviewClt.Create_LanView_Pload(reqID=item)
            resBody = self.LanviewClt.lanView(cookies=self.cookie, pload=pload).body
            resbody_Lst.append(resBody)

        self.LanviewClt.assert_response_list(resbody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])