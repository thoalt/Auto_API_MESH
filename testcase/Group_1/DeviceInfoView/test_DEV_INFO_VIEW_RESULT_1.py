import time
import pytest

from APIObject.deviceInfoView import deviceInfoViewClient
from Config import Schema_Template as scTmp
from pages.HomePage import HomePage

@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_DeviceInfoView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success", "action": "deviceInfoView"}
        self.devInf = deviceInfoViewClient()

        # Setting Location
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_device_info_setting_page()
        self.hp.set_device_info(location="VNPT_Technology")
        time.sleep(10)


    def test_DEV_INFO_VIEW_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.devInf.deviceInfoView(self.cookie).body
        self.devInf.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])
        self.devInf.valid_schema_resul(resBody, schema=scTmp.schema_deviceInfoView_result)