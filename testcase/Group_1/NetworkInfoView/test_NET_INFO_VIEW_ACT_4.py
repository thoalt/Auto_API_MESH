import time
import pytest
from APIObject.networkinfoView import networkinfoViewClient


@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.netInf = networkinfoViewClient()
        self.data = ['']



    def test_DEV_INFO_VIEW_ACT_4(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.netInf.Create_networkinfoView_Pload(action=item)
            resBody = self.netInf.networkinfoView(self.cookie,pload=pload).body
            resBody_Lst.append(resBody)
        self.netInf.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
