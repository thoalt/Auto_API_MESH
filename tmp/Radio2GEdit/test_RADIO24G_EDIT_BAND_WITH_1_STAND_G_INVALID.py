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

        self.radio24GEditClt = radio24GEditClient()
        self.radio2GViewClt = radio24GViewClient()
        self.wrp = WirelessRadioPage(self.driver)
        # Setting for Radio 2.4G with standard mode NG
        self.wrp.setting_Radio(bandW=WIFI_TYPE.T_24G, standard=STANDARD_2G.MOD_G)
        time.sleep(self.timeOut)

        self.channel = CHANNEL_API.C_AUTO

        self.bandwith_API_lst = [BAND_WITH_API.B_40,
                                 BAND_WITH_API.B_20_40]

        self.bandwith_GUI_exp = [BAND_WITH_GUI.B_20,
                                 BAND_WITH_GUI.B_20_40]

    def test_RADIO24G_EDIT_RES_6(self):
        resBody_lst = []
        bandwithGUI_actual_lst = []
        for item in self.bandwith_API_lst:
            # Setting Bandwith via API
            pload = self.radio24GEditClt.Create_radio24GEdit_Pload(channel=self.channel, bandW=item)
            resBodyApply = self.radio24GEditClt.radio24GEdit(self.cookie, pload=pload).body

            # Wait 60s to apply configuration
            time.sleep(self.timeOut)

            # Getting Bandwith via Radio 2G View
            resBody = self.radio2GViewClt.radio24GView(self.cookie).body
            resBody_lst.append(resBody)

            # Getting Bandwith via WebGui
            self.wrp.navigate_to_radio_2G_page()
            bandwith = self.wrp.get_Bandwith2G_sp()
            bandwithGUI_actual_lst.append(bandwith)

        # Verify the result Get from API
        self.radio2GViewClt.assert_result_lst(resBody_lst,
                                       bandWLst=self.bandwith_API_lst)

        # Verify the result Get from GUI
        self.radio2GViewClt.assert_val_lst(self.bandwith_GUI_exp, bandwithGUI_actual_lst)
