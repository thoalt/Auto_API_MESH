import time
import pytest
from APIObject.wifi24GAPI import radio24GEditClient, radio24GViewClient
from APIObject.wifi24GAPI import CHANNEL_API, BAND_WITH_API
from pages.SettingWirelessPage import WirelessRadioPage, CHANNEL_GUI, BAND_WITH_GUI, WIFI_TYPE, STANDARD_2G
from base.WiFiLib import Wifi_lib
from base.SSHLib import SSH_Lib
from Config import config as cfg

@pytest.mark.usefixtures("login", "login_CAP_GUI", "create_shell")
class Test_radio24G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.standard = STANDARD_2G.MOD_NG
        self.radio24GEditClt = radio24GEditClient()
        self.radio2GViewClt = radio24GViewClient()

        self.client2G = Wifi_lib()
        self.session = SSH_Lib(SSHShell=self.SSHShell)

        self.wrp = WirelessRadioPage(self.driver)
        self.wrp.navigate_to_radio_2G_setting_page()
        self.wrp.setting_Radio(bandW=WIFI_TYPE.T_24G, standard=self.standard)
        time.sleep(self.timeOut)

        self.channel = CHANNEL_API.C_AUTO

        self.bandwith_API_lst = [BAND_WITH_API.B_20,
                                 BAND_WITH_API.B_20_40]

        self.bandwith_GUI_exp = [BAND_WITH_GUI.B_20,
                                 BAND_WITH_GUI.B_20_40]

    def test_RADIO24G_EDIT_RES_6(self):
        resBody_lst = []
        bandwithGUI_actual_lst = []
        bandW_Driver_Actual_lst = []

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
            self.wrp.navigate_to_radio_2G_setting_page()
            bandwith = self.wrp.get_Bandwith2G_sp()
            bandwithGUI_actual_lst.append(bandwith)

            # Getting Bandwidth from driver
            bitrate = self.session.get_bitrate(cfg.WIFI_INT_2G)
            bandW = self.client2G.Convert_Bitrate_To_Bandwith(standard=self.standard, bitrate=bitrate)
            bandW_Driver_Actual_lst.append(bandW)

        # Verify the result Get from API
        self.radio2GViewClt.assert_result_lst(resBody_lst,
                                       bandWLst=self.bandwith_API_lst)

        # Verify the result Get from GUI
        self.radio2GViewClt.assert_val_lst(self.bandwith_GUI_exp, bandwithGUI_actual_lst)

       # Verify the result get from driver
        self.radio2GViewClt.assert_val_lst( self.bandwith_API_lst, bandW_Driver_Actual_lst)