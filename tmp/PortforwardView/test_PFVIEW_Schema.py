import time
import pytest
from APIObject.serviceAPI import portforwardViewClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_portView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.portViewClt = portforwardViewClient()

    @pytest.mark.success
    def test_portView_Schema(self):
        time.sleep(self.timeOut)
        resBody = self.portViewClt.portforwardView(self.cookie).body
        #self.portViewClt.assert_response(resBody,
                                        #self.exp['code'],
                                        #self.exp['msg'],
                                        #self.exp['action'])
        self.portViewClt.valid_schema_common(resBody)
        self.portViewClt.valid_schema_resul(resBody, schema=scTmp.schema_portforwardView_result)
