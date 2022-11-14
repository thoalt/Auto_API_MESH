import time
import pytest
from APIObject.wifi24GAPI import radio24GEditClient, radio24GViewClient
from APIObject.wifi24GAPI import CHANNEL_API, BAND_WITH_API
from pages.SettingWirelessPage import WirelessRadioPage, CHANNEL_GUI, BAND_WITH_GUI
from base.WiFiLib import Wifi_lib
from base.SSHLib import SSH_Lib
from Config import config as cfg

@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_radio24G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60

        self.radio24GEditClt = radio24GEditClient()
        self.radio2GViewClt = radio24GViewClient()
        self.wrp = WirelessRadioPage(self.driver)
        self.client2G = Wifi_lib()
        self.session = SSH_Lib(SSHShell=self.SSHShell)

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

        self.bandWith = BAND_WITH_API.B_20

    def test_RADIO24G_EDIT_RES_6(self):
        resBody_lst = []
        channelGUI_actual_lst = []
        channelDriver_actual_lst = []

        for item in self.channel_API_lst:
            # Setting Channel via API
            pload = self.radio24GEditClt.Create_radio24GEdit_Pload(channel=item, bandW=self.bandWith)
            resBodyApply = self.radio24GEditClt.radio24GEdit(self.cookie, pload=pload).body

            # Wait 60s to apply configuration
            time.sleep(self.timeOut)

            # Getting Channel via Radio 2G View
            resBody = self.radio2GViewClt.radio24GView(self.cookie).body
            resBody_lst.append(resBody)

            # Getting Channel via WebGui
            self.wrp.navigate_to_radio_2G_page()
            channel = self.wrp.get_Channel2G_sp()
            channelGUI_actual_lst.append(channel)

            # Getting Channel from driver
            channel = self.session.get_channel(cfg.WIFI_INT_2G)
            channelDriver_actual_lst.append(channel)

        # Verify the result Get from API
        self.radio2GViewClt.assert_result_lst(resBody_lst,
                                       channelLst=self.channel_API_lst)

        # Verify the result Get from GUI
        self.radio2GViewClt.assert_val_lst(self.channel_GUI_exp, channelGUI_actual_lst)

        # Verify the result Get from Driver
        self.radio2GViewClt.assert_val_lst(self.channel_API_lst, channelDriver_actual_lst)
