import time
import pytest
from APIObject.networkinfoView import networkinfoViewClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_NetworkInfo():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.netInfo = networkinfoViewClient()

    def test_NetworkInfo_Schema(self):
        time.sleep(self.timeOut)
        resBody = self.netInfo.networkinfoView(self.cookie).body

        self.netInfo.valid_schema_common(resBody)
        self.netInfo.valid_schema_resul(resBody, schema=scTmp.schema_networkinfoView_result, require_all=False)

