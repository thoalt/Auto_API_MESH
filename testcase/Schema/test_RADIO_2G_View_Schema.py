import time
import pytest
from APIObject.radio24GView import radio24GViewClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_Radio2GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.radio2G = radio24GViewClient()

    def test_Radio2GView_Schema(self):
        time.sleep(self.timeOut)
        resBody = self.radio2G.radio24GView(self.cookie).body

        self.radio2G.valid_schema_common(resBody)
        self.radio2G.valid_schema_resul(resBody, schema=scTmp.schema_radio24GView_result)

