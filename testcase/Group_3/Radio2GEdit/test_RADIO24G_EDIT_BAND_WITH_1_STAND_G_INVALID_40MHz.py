import time
import pytest
from APIObject.wifi24GAPI import radio24GEditClient, radio24GViewClient
from APIObject.wifi24GAPI import CHANNEL_API, BAND_WITH_API
from pages.SettingWirelessPage import WirelessRadioPage, CHANNEL_GUI, BAND_WITH_GUI, WIFI_TYPE, STANDARD_2G


@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_radio24G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.standard = STANDARD_2G.MOD_G

        self.radio24GEditClt = radio24GEditClient()
        self.radio2GViewClt = radio24GViewClient()
        self.wrp = WirelessRadioPage(self.driver)

        # Setting for Radio 2.4G with standard mode NG
        self.wrp.navigate_to_radio_2G_setting_page()
        self.wrp.setting_Radio(bandW=WIFI_TYPE.T_24G, standard= self.standard)
        time.sleep(self.timeOut)

        self.channel = CHANNEL_API.C_AUTO
        self.bandwith_API_lst = [BAND_WITH_API.B_40,
                                 BAND_WITH_API.B_80]

    def test_RADIO24G_EDIT_RES_6(self):
        resBody_Lst = []

        for item in self.bandwith_API_lst:
            # Setting Bandwith via API
            pload = self.radio24GEditClt.Create_radio24GEdit_Pload(channel=self.channel, bandW=item)
            resBodyApply = self.radio24GEditClt.radio24GEdit(self.cookie, pload=pload).body

            resBody_Lst.append(resBodyApply)
            time.sleep(2)
        self.radio24GEditClt.assert_response_list(resBody_Lst,
                                                 self.exp['code'],
                                                 self.exp['msg'])