import time
import pytest
from APIObject.wanViewConfig import WanViewClient

@pytest.mark.usefixtures("login")
class Test_Wanview():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.data = [2147483648]
        self.WanviewClt = WanViewClient()

    @pytest.mark.success
    def test_WANVIEW_REQID_4(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.WanviewClt.Create_WanView_Pload(reqID=item)
            resBody = self.WanviewClt.wanViewConfig(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)
        self.WanviewClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])


