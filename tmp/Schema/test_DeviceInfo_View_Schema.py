import time
import pytest
from APIObject.deviceInfoView import deviceInfoViewClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_DeviceInfo():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.devInfo = deviceInfoViewClient()

    def test_Radio2GView_Schema(self):
        time.sleep(self.timeOut)
        resBody = self.devInfo.deviceInfoView(self.cookie).body

        self.devInfo.valid_schema_common(resBody)
        self.devInfo.valid_schema_resul(resBody, schema=scTmp.schema_deviceInfoView_result)

