import time
import pytest
from APIObject.wifi5GAPI import radio5GEditClient, radio5GViewClient
from APIObject.wifi5GAPI import CHANNEL_API, BAND_WIDTH_API
from pages.SettingWirelessPage import WirelessRadioPage, CHANNEL_GUI, BAND_WITH_GUI,  WIFI_TYPE, STANDARD_5G
from base.WiFiLib import Wifi_lib
from base.SSHLib import SSH_Lib
from Config import config as cfg

@pytest.mark.usefixtures("login")
class Test_radio5G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60

        self.channel = CHANNEL_API.C_AUTO
        self.bandWith = BAND_WIDTH_API.B_20

        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.data = ['',
                     "20mhz", "40mhz", "80mhz",
                     '20MHZ', '40MHZ', "80MHZ",
                     "20 MHz", "40 MHz", "80 MHz",
                     "20", "40", "80",
                     20, 40, 80]

        self.radio5GEditClt = radio5GEditClient()


    def test_RADIO5G_EDIT_BW_1(self):
        time.sleep(self.timeOut)
        resBody_lst = []

        for item in self.data:
            # Setting Channel via API
            pload = self.radio5GEditClt.Create_Radio5GEdit_Pload(channel=self.channel, bandW=item)
            resBody = self.radio5GEditClt.radio5GEdit(self.cookie, pload=pload).body
            resBody_lst.append(resBody)

        self.radio5GEditClt.assert_response_list(resBody_lst,
                                            self.exp['code'],
                                            self.exp['msg'])