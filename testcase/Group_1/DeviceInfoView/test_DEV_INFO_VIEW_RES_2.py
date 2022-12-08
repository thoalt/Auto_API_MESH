import time
import pytest

from APIObject.deviceInfoView import deviceInfoViewClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 590
        self.exp = {"code": 0, "msg": "Success", "action": "deviceInfoView"}
        self.devInf = deviceInfoViewClient()

    def test_DEV_INFO_VIEW_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.devInf.deviceInfoView(self.cookie).body
        self.devInf.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])