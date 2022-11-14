import time
import pytest
from APIObject.wifi5GAPI import radio5GEditClient, CHANNEL_API, BAND_WIDTH_API

@pytest.mark.usefixtures("login")
class Test_radio5G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 10, "msg": "Miss Attribute"}

        self.radio5GEditClt = radio5GEditClient()
        self.channel = CHANNEL_API.C_36
        self.bandWith = BAND_WIDTH_API.B_20

        pload = self.radio5GEditClt.Create_Radio5GEdit_Pload(channel=self.channel, bandW=self.bandWith)
        self.data = self.radio5GEditClt.Remove_Attribute_In_Pload(pload)

    @pytest.mark.success
    def test_RADIO5G_EDIT_RES_6(self):
        time.sleep(self.timeOut)
        resBody_Lst = []
        for item in self.data:
            resBody = self.radio5GEditClt.radio5GEdit(self.cookie, pload=item).body
            resBody_Lst.append(resBody)

        self.radio24GEditClt.assert_response_list(resBody_Lst,
                                                self.exp['code'],
                                                self.exp['msg'])

