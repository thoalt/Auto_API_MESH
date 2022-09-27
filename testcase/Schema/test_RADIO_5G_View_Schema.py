import time
import pytest
from APIObject.wifi5GAPI import radio5GViewClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_Radio2GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.radio5G = radio5GViewClient()

    def test_Radio2GView_Schema(self):
        time.sleep(self.timeOut)
        resBody = self.radio5G.radio5GView(self.cookie).body

        self.radio5G.valid_schema_common(resBody)
        self.radio5G.valid_schema_resul(resBody, schema=scTmp.schema_radio5GView_result)

