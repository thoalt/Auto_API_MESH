import time
import pytest
from APIObject.wifi5GAPI import radio5GEditClient, radio5GViewClient
from APIObject.wifi5GAPI import CHANNEL_API, BAND_WIDTH_API
from pages.SettingWirelessPage import WirelessRadioPage, CHANNEL_GUI, BAND_WITH_GUI,  WIFI_TYPE, STANDARD_5G
from base.WiFiLib import Wifi_lib
from base.SSHLib import SSH_Lib
from Config import config as cfg

@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_radio5G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.standard = STANDARD_5G.MOD_NA

        self.radio5GEditClt = radio5GEditClient()
        self.radio5GViewClt = radio5GViewClient()
        self.wrp = WirelessRadioPage(self.driver)

        #Setting for Radio 5G with standard mode 11a
        self.wrp.navigate_to_radio_5G_setting_page()
        self.wrp.setting_Radio(bandW=WIFI_TYPE.T_5G, standard=self.standard)
        time.sleep(self.timeOut)

        self.channel = CHANNEL_API.C_165
        self.bandwith_API_lst = [BAND_WIDTH_API.B_40,
                                 BAND_WIDTH_API.B_80]
        self.bandwith_GUI_exp = [BAND_WITH_GUI.B_40,
                                 BAND_WITH_GUI.B_80]

    def test_RADIO5G_EDIT_BW_1(self):
        resBody_Lst = []

        for item in self.bandwith_API_lst:
            # Setting Channel via API
            pload = self.radio5GEditClt.Create_Radio5GEdit_Pload(channel=self.channel, bandW=item)
            resBodyApply = self.radio5GEditClt.radio5GEdit(self.cookie, pload=pload).body

            resBody_Lst.append(resBodyApply)
            time.sleep(2)
        self.radio5GEditClt.assert_response_list(resBody_Lst,
                                                 self.exp['code'],
                                                 self.exp['msg'])