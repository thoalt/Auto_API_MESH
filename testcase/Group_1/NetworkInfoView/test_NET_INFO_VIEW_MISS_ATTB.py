import time
import pytest
from APIObject.networkinfoView import networkinfoViewClient


@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 10, "msg": "Miss Attribute"}
        self.netInf = networkinfoViewClient()
        pload = self.netInf.Create_networkinfoView_Pload()
        self.data = [self.netInf.Remove_Key_In_Pload(pload, 'action')]


    def test_DEV_INFO_VIEW_ACT_2(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            resBody = self.netInf.networkinfoView(self.cookie,pload=item).body
            resBody_Lst.append(resBody)
        self.netInf.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])
