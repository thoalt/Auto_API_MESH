import time
import pytest

from APIObject.deviceInfoView import deviceInfoViewClient
from Utilities import Utility as ult

@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 9, "msg": "Miss Request ID"}
        self.devInf = deviceInfoViewClient()
        pload: dict = self.devInf.Create_deviceInfoView_Pload()
        self.pload_lst = [self.devInf.Remove_Key_In_Pload(pload, 'requestId')]


    def test_DEV_INFO_MISS_ATB_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.pload_lst:
            resBody = self.devInf.deviceInfoView(self.cookie, pload=item).body
            resBody_lst.append(resBody)

        self.devInf.assert_response_list(resBody_lst,
                                    self.exp['code'],
                                    self.exp['msg'])