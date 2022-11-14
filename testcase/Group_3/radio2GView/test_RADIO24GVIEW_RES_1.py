import time
import pytest
from APIObject.wifi24GAPI import radio24GViewClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_radio24GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code":0 , "msg": "Success", "action": "radio2.4GView"}
        self.radio24GViewClt = radio24GViewClient()


    def test_RADIO24GVIEW_RES_6(self):
          time.sleep(self.timeOut)
          resBody = self.radio24GViewClt.radio24GView(self.cookie).body
          self.radio24GViewClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

          self.radio24GViewClt.valid_schema_common(resBody)
          self.radio24GViewClt.valid_schema_resul(resBody, schema=scTmp.schema_radio24GView_result)
