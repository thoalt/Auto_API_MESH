import time
import pytest
from APIObject.wifi5GAPI import radio5GEditClient, CHANNEL_API, BAND_WIDTH_API

@pytest.mark.usefixtures("login")
class Test_radio5G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ["ă", "â", "đ", "ê", "ô", "ơ", "ư", "á", "à", "ạ", "ả", "ã",
                     "Ă", "Â", "Đ", "Ê", "Ô", "Ơ", "Ư", "Á", "À", "Ạ", "Ả", "Ã"]

        self.radio5GEditClt = radio5GEditClient()
        self.channel = CHANNEL_API.C_36
        self.bandWith = BAND_WIDTH_API.B_20

    @pytest.mark.success
    def test_RADIO5G_EDIT_RES_6(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            pload = self.radio5GEditClt.Create_Radio5GEdit_Pload(action=item, channel=self.channel, bandW=self.bandWith)
            resBody = self.radio5GEditClt.radio5GEdit(self.cookie, pload=pload).body
            resBody_Lst.append(resBody)

        self.radio24GEditClt.assert_response_list(resBody_Lst,
                                                self.exp['code'],
                                                self.exp['msg'])

