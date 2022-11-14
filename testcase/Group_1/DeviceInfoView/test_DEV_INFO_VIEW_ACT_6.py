import time
import pytest
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.wanAPI import WanViewConfigClient
from APIObject.deviceInfoView import deviceInfoViewClient


@pytest.mark.usefixtures("login")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ["“", "‘", "|", "/", "\\", ",", ";", ":", "&", "<", ">", "^", "*", "?"]
        self.devInf = deviceInfoViewClient()

    def test_DEV_INFO_VIEW_ACT_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []
        for item in self.data:
            pload = self.devInf.Create_deviceInfoView_Pload(action=item)
            resBody = self.devInf.deviceInfoView(cookies=self.cookie, pload=pload).body
            resBody_lst.append(resBody)
        self.devInf.assert_response_list(resBody_lst,
                                           self.exp['code'],
                                           self.exp['msg'])