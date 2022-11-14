import time
import pytest
from APIObject.wifi24GAPI import ssid24GViewClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_ssid24GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.ssid24GViewClt = ssid24GViewClient()

    def test_ssid24GView_Schema(self):
        time.sleep(self.timeOut)
        resBody = self.ssid24GViewClt.ssid24GView(self.cookie).body

        self.ssid24GViewClt.valid_schema_common(resBody)
        self.ssid24GViewClt.valid_schema_resul(resBody, schema=scTmp.schema_ssidView_result)


