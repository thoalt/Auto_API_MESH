import time
import pytest
from APIObject.wifi24GAPI import radio24GEditClient, radio24GViewClient
from APIObject.wifi24GAPI import CHANNEL_API, BAND_WITH_API
from pages.SettingWirelessPage import WirelessRadioPage, CHANNEL_GUI, BAND_WITH_GUI, STANDARD_2G, WIFI_TYPE
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

        # Setting for Radio 2.4G with standard mode NG
        self.wrp.setting_Radio(bandW=WIFI_TYPE.T_24G, standard=self.standard)
        time.sleep(self.timeOut)

        self.channel_API_lst = [CHANNEL_API.C_AUTO,
                                CHANNEL_API.C_1,
                                CHANNEL_API.C_2,
                                CHANNEL_API.C_3,
                                CHANNEL_API.C_4,
                                CHANNEL_API.C_5,
                                CHANNEL_API.C_6,
                                CHANNEL_API.C_7,
                                CHANNEL_API.C_8,
                                CHANNEL_API.C_9,
                                CHANNEL_API.C_10,
                                CHANNEL_API.C_11]

        self.channel_GUI_exp = [CHANNEL_GUI.C_AUTO,
                                CHANNEL_GUI.C_1,
                                CHANNEL_GUI.C_2,
                                CHANNEL_GUI.C_3,
                                CHANNEL_GUI.C_4,
                                CHANNEL_GUI.C_5,
                                CHANNEL_GUI.C_6,
                                CHANNEL_GUI.C_7,
                                CHANNEL_GUI.C_8,
                                CHANNEL_GUI.C_9,
                                CHANNEL_GUI.C_10,
                                CHANNEL_GUI.C_11]

        self.bandwith_API_lst = [BAND_WITH_API.B_20,
                                 BAND_WITH_API.B_20_40]

        self.bandwith_GUI_exp = [BAND_WITH_GUI.B_20,
                                 BAND_WITH_GUI.B_20_40]

    def test_RADIO24G_EDIT_RES_6(self):
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
                pload = self.radio24GEditClt.Create_radio24GEdit_Pload(channel=channel, bandW=bw)
                resBodyApply = self.radio24GEditClt.radio24GEdit(self.cookie, pload=pload).body

                # Wait 60s to apply configuration
                time.sleep(self.timeOut)

                # Getting Bandwith via Radio 2G View
                resBody = self.radio2GViewClt.radio24GView(self.cookie).body
                resBody_lst.append(resBody)

                # Getting Bandwith via WebGui
                self.wrp.navigate_to_radio_2G_setting_page()
                bandwithGUI = self.wrp.get_Bandwith2G_sp()
                channelGUI = self.wrp.get_Channel2G_sp()

                bandwithGUI_actual_lst.append(bandwithGUI)
                channelGUI_actula_lst.append(channelGUI)

                # Getting via driver
                bitrate = self.session.get_bitrate(cfg.WIFI_INT_2G)
                bandwithDriver = self.client2G.Convert_Bitrate_To_Bandwith(standard=self.standard, bitrate=bitrate)
                channelDriver = self.session.get_channel(cfg.WIFI_INT_2G)

                bandwithDriver_actual_lst.append(bandwithDriver)
                channelDriver_actula_lst.append(channelDriver)


        # Verify the result Get from API
        # Compare the result get from API with the value setting
        self.radio2GViewClt.assert_result_lst(resBody_lst,
                                              channelLst=channel_setting_lst,
                                              bandWLst=bw_setting_lst)

        # Verify the result Get from GUI
        self.radio2GViewClt.assert_val_lst(bandwithGUI_exp_lst, bandwithGUI_actual_lst)
        self.radio2GViewClt.assert_val_lst(channelGUI_exp_lst, channelGUI_actula_lst)

        # Verify the result Get from Driver
        # self.radio2GViewClt.assert_val_lst(bw_setting_lst, bandwithDriver_actual_lst)
        self.radio2GViewClt.assert_val_lst(channel_setting_lst, channelDriver_actula_lst)