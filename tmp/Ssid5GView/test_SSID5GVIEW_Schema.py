import time
import pytest
from APIObject.wifi5GAPI import ssid5GViewClient
from Config import Schema_Template as scTmp


@pytest.mark.usefixtures("login")
class Test_ssid5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.ssid5GViewClt = ssid5GViewClient()

    @pytest.mark.success
    def test_ssid5GView_Schema(self):
        time.sleep(self.timeOut)
        resBody = self.ssid5GViewClt.ssid5GView(self.cookie).body
        self.ssid5GViewClt.valid_schema_common()
        self.ssid5GViewClt.valid_schema_resul(resBody, schema=scTmp.schema_ssidView_result)
