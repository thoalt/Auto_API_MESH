import time
import pytest
from APIObject.wifi24GAPI import radio24GEditClient, CHANNEL_API, BAND_WITH_API

@pytest.mark.usefixtures("login")
class Test_radio24G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 610
        self.exp = {"code": 15, "msg": "Session Timeout"}
        self.radio24GEditClt = radio24GEditClient()
        self.channel = CHANNEL_API.C_1
        self.bandWith = BAND_WITH_API.B_20

    def test_RADIO24G_EDIT_RES_6(self):
          time.sleep(self.timeOut)
          pload = self.radio24GEditClt.Create_radio24GEdit_Pload(channel=self.channel, bandW=self.bandWith)
          resBody = self.radio24GEditClt.radio24GEdit(self.cookie, pload=pload).body
          self.radio24GEditClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])

