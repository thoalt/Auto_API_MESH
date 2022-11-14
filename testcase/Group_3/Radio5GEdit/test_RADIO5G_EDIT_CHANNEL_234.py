import time
import pytest
from APIObject.wifi5GAPI import radio5GEditClient, radio5GViewClient
from APIObject.wifi5GAPI import CHANNEL_API, BAND_WIDTH_API

@pytest.mark.usefixtures("login")
class Test_radio5G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.bandWith = BAND_WIDTH_API.B_20
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.radio5GEditClt = radio5GEditClient()

        self.channel_API_lst = ['', 0, 12, -1, 1.0, 11.0, 165.0,
                                36, 40, 44, 48, 52, 56, 60, 64,
                                100, 104, 112, 116, 120, 124, 128, 132, 136, 140, 144,
                                149, 153, 157, 161, 165]

    def test_RADIO24G_EDIT_CHANNEL_1(self):
        resBody_lst = []

        for item in self.channel_API_lst:
            # Setting Channel via API
            pload = self.radio5GEditClt.Create_Radio5GEdit_Pload(channel=item, bandW=self.bandWith)
            resBody = self.radio5GEditClt.radio5GEdit(self.cookie, pload=pload).body
            resBody_lst.append(resBody)

        # Verify the result Get from API
        self.radio5GEditClt.assert_response_list(resBody_lst,
                                            self.exp['code'],
                                            self.exp['msg'])