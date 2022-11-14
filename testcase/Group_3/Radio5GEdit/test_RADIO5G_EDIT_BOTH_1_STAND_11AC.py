import time
import pytest
from APIObject.wifi5GAPI import radio5GEditClient, radio5GViewClient
from APIObject.wifi5GAPI import CHANNEL_API, BAND_WIDTH_API
from pages.SettingWirelessPage import WirelessRadioPage, CHANNEL_GUI, BAND_WITH_GUI, STANDARD_5G, WIFI_TYPE
from base.WiFiLib import Wifi_lib
from base.SSHLib import SSH_Lib
from Config import config as cfg

@pytest.mark.usefixtures("login", "login_CAP_GUI", "create_shell")
class Test_radio5G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.standard = STANDARD_5G.MOD_AC
        self.radio5GEditClt = radio5GEditClient()
        self.radio5GViewClt = radio5GViewClient()
        self.client5G = Wifi_lib()
        self.session = SSH_Lib(SSHShell=self.SSHShell)
        self.wrp = WirelessRadioPage(self.driver)
        self.wrp.navigate_to_radio_5G_setting_page()

        # Setting for Radio 2.4G with standard mode NG
        self.wrp.setting_Radio(bandW=WIFI_TYPE.T_5G, standard=self.standard)
        time.sleep(self.timeOut)

        self.channel_API_lst = ["auto", "36", "40", "44", "48", "52", "56", "60", "64", "100", "104", "112", "116",
                                "120", "124", "128", "132", "136", "140", "144", "149", "153", "157", "161"]

        self.channel_GUI_exp = ["Auto", "36", "40", "44", "48", "52", "56", "60", "64", "100", "104", "112", "116",
                                "120", "124", "128", "132", "136", "140", "144", "149", "153", "157", "161"]

        self.bandwith_API_lst = [BAND_WIDTH_API.B_20,
                                 BAND_WIDTH_API.B_40,
                                 BAND_WIDTH_API.B_80]
        self.bandwith_GUI_exp = [BAND_WITH_GUI.B_20,
                                 BAND_WITH_GUI.B_40,
                                 BAND_WITH_GUI.B_80]
        

    def test_radio5G_EDIT_RES_6(self):
        resBody_lst = []

        bandwithGUI_actual_lst = []
        channelGUI_actula_lst = []

        bandwithDriver_actual_lst = []
        channelDriver_actula_lst = []

        bandwithGUI_exp_lst = []
        channelGUI_exp_lst = []

        channel_setting_lst = []
        bw_setting_lst = []

        #### GET EXPECTED LIST OF GUI
        for channel in self.channel_GUI_exp:
            for bw in self.bandwith_GUI_exp:
                channelGUI_exp_lst.append(channel)
                bandwithGUI_exp_lst.append(bw)

        ## SETTING
        for channel in self.channel_API_lst:
            for bw in self.bandwith_API_lst:
                channel_setting_lst.append(channel)
                bw_setting_lst.append(bw)

                # Setting Bandwith via API
                pload = self.radio5GEditClt.Create_Radio5GEdit_Pload(channel=channel, bandW=bw)
                resBodyApply = self.radio5GEditClt.radio5GEdit(self.cookie, pload=pload).body

                # Wait 60s to apply configuration
                time.sleep(self.timeOut)

                # Getting Bandwith via Radio 2G View
                resBody = self.radio5GViewClt.radio5GView(self.cookie).body
                resBody_lst.append(resBody)

                # Getting Bandwith via WebGui
                self.wrp.navigate_to_radio_5G_setting_page()
                bandwithGUI = self.wrp.get_Bandwith5G_sp()
                channelGUI = self.wrp.get_Channel5G_sp()

                bandwithGUI_actual_lst.append(bandwithGUI)
                channelGUI_actula_lst.append(channelGUI)

                # Getting via driver
                bitrate = self.session.get_bitrate(cfg.WIFI_INT_5G)
                bandwithDriver = self.client5G.Convert_Bitrate_To_Bandwith(standard=self.standard, bitrate=bitrate)
                channelDriver = self.session.get_channel(cfg.WIFI_INT_5G)
                if channel == 'auto':
                    channelDriver = 'auto'
                bandwithDriver_actual_lst.append(bandwithDriver)
                channelDriver_actula_lst.append(channelDriver)


        # Verify the result Get from API
        # Compare the result get from API with the value setting
        self.radio5GViewClt.assert_result_lst(resBody_lst,
                                              channelLst=channel_setting_lst,
                                              bandWLst=bw_setting_lst)

        # Verify the result Get from GUI
        self.radio5GViewClt.assert_val_lst(bandwithGUI_exp_lst, bandwithGUI_actual_lst)
        self.radio5GViewClt.assert_val_lst(channelGUI_exp_lst, channelGUI_actula_lst)

        # Verify the result Get from Driver
        self.radio5GViewClt.assert_val_lst(bw_setting_lst, bandwithDriver_actual_lst)
        self.radio5GViewClt.assert_val_lst(channel_setting_lst, channelDriver_actula_lst)