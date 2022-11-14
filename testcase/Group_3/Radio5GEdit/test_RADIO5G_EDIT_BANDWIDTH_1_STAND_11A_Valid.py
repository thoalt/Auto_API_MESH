import time
import pytest
from APIObject.wifi5GAPI import radio5GEditClient, radio5GViewClient
from APIObject.wifi5GAPI import CHANNEL_API, BAND_WIDTH_API
from pages.SettingWirelessPage import WirelessRadioPage, CHANNEL_GUI, BAND_WITH_GUI,  WIFI_TYPE, STANDARD_5G
from base.WiFiLib import Wifi_lib
from base.SSHLib import SSH_Lib
from Config import config as cfg

@pytest.mark.usefixtures("login", "login_CAP_GUI","create_shell")
class Test_radio5G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.standard = STANDARD_5G.MOD_A

        self.radio5GEditClt = radio5GEditClient()
        self.radio5GViewClt = radio5GViewClient()
        self.wrp = WirelessRadioPage(self.driver)

        self.client5G = Wifi_lib()
        self.session = SSH_Lib(SSHShell=self.SSHShell)

        #Setting for Radio 5G with standard mode 11a
        self.wrp.navigate_to_radio_5G_setting_page()
        self.wrp.setting_Radio(bandW=WIFI_TYPE.T_5G, standard=self.standard)
        time.sleep(self.timeOut)

        self.channel = CHANNEL_API.C_36
        self.bandwith_API_lst = [BAND_WIDTH_API.B_20]
        self.bandwith_GUI_exp = [BAND_WITH_GUI.B_20]

    def test_RADIO5G_EDIT_BW_1(self):
        resBody_lst = []
        bandwithGUI_actual_lst = []
        bandW_Driver_Actual_lst = []

        for item in self.bandwith_API_lst:
            # Setting Channel via API
            pload = self.radio5GEditClt.Create_Radio5GEdit_Pload(channel=self.channel, bandW=item)
            resBodyApply = self.radio5GEditClt.radio5GEdit(self.cookie, pload=pload).body

            # Wait 60s to apply configuration
            time.sleep(self.timeOut)

            # Getting Channel via Radio 5G View
            resBody = self.radio5GViewClt.radio5GView(self.cookie).body
            resBody_lst.append(resBody)

            # Getting Channel from driver
            bitrate = self.session.get_bitrate(cfg.WIFI_INT_5G)
            bandW = self.client5G.Convert_Bitrate_To_Bandwith(standard=self.standard, bitrate=bitrate)
            bandW_Driver_Actual_lst.append(bandW)

            # Getting Channel via WebGui
            self.wrp.navigate_to_radio_5G_setting_page()
            bandwith = self.wrp.get_Bandwith5G_sp()
            bandwithGUI_actual_lst.append(bandwith)
            # Click to tab Radio 5G again
            # self.wrp.click_Radio5G()

        # Verify the result Get from API
        self.radio5GViewClt.assert_result_lst(resBody_lst,
                                        bandWLst=self.bandwith_API_lst)

        # Verify the result Get from GUI
        self.radio5GViewClt.assert_val_lst(self.bandwith_GUI_exp, bandwithGUI_actual_lst)

        # # Verify the result Get from Driver
        # self.radio5GViewClt.assert_val_lst(self.bandwith_API_lst, bandW_Driver_Actual_lst)
