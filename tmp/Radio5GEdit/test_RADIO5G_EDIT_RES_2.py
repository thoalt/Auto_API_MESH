import time
import pytest
from APIObject.wifi5GAPI import radio5GEditClient, CHANNEL_API, BAND_WIDTH_API

@pytest.mark.usefixtures("login")
class Test_radio5G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 590
        self.exp = {"code": 0, "msg": "Success"}
        self.radio5GEditClt = radio5GEditClient()
        self.channel = CHANNEL_API.C_36
        self.bandWith = BAND_WIDTH_API.B_20

    @pytest.mark.success
    def test_RADIO5G_EDIT_RES_6(self):
          time.sleep(self.timeOut)
          pload = self.radio5GEditClt.Create_Radio5GEdit_Pload(channel=self.channel, bandW=self.bandWith)
          resBody = self.radio5GEditClt.radio5GEdit(self.cookie, pload=pload).body
          self.radio5GEditClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])

