import time
import pytest
from APIObject.wifi24GAPI import radio24GEditClient, CHANNEL_API, BAND_WITH_API

@pytest.mark.usefixtures("login")
class Test_radio24G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ["ă", "â", "đ", "ê", "ô", "ơ", "ư", "á", "à", "ạ", "ả", "ã",
                     "Ă", "Â", "Đ", "Ê", "Ô", "Ơ", "Ư", "Á", "À", "Ạ", "Ả", "Ã"]
        self.radio24GEditClt = radio24GEditClient()
        self.channel = CHANNEL_API.C_1
        self.bandWith = BAND_WITH_API.B_20

    def test_RADIO24G_EDIT_RES_6(self):
          time.sleep(self.timeOut)
          resBody_Lst = []
          for item in self.data:
              pload = self.radio24GEditClt.Create_radio24GEdit_Pload(action=item, channel=self.channel, bandW=self.bandWith)
              resBody = self.radio24GEditClt.radio24GEdit(self.cookie, pload=pload).body
              resBody_Lst.append(resBody)

          self.radio24GEditClt.assert_response_list(resBody_Lst,
                                        self.exp['code'],
                                        self.exp['msg'])

