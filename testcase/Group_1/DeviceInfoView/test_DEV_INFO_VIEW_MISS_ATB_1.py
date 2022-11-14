import time
import pytest

from APIObject.deviceInfoView import deviceInfoViewClient

@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 10, "msg": "Miss Attribute"}
        self.devInf = deviceInfoViewClient()
        pload: dict = self.devInf.Create_deviceInfoView_Pload()
        self.data = [self.devInf.Remove_Key_In_Pload(pload, 'action')]


    def test_DEV_INFO_MISS_ATB_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            resBody = self.devInf.deviceInfoView(self.cookie, pload=item).body
            resBody_lst.append(resBody)

        self.devInf.assert_response_list(resBody_lst,
                                    self.exp['code'],
                                    self.exp['msg'])