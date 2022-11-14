import time
import pytest
from APIObject.wifi24GAPI import radio24GEditClient, radio24GViewClient
from APIObject.wifi24GAPI import CHANNEL_API, BAND_WITH_API

@pytest.mark.usefixtures("login")
class Test_TraceRoute():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.bandWith = BAND_WITH_API.B_20
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        self.radio24GEditClt = radio24GEditClient()

    @pytest.mark.success
    def test_RADIO2G_EDIT_CHANNEL_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []

        for item in self.data:
            pload = self.radio24GEditClt.Create_radio24GEdit_Pload(channel=item, bandW=self.bandWith)
            resBody = self.radio24GEditClt.radio24GEdit(self.cookie, pload=pload).body
            resBody_lst.append(resBody)

        self.radio24GEditClt.assert_response_list(resBody_lst,
                                            self.exp['code'],
                                            self.exp['msg'])


