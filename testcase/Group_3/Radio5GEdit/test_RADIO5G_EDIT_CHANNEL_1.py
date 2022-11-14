import time
import pytest
from APIObject.wifi5GAPI import radio5GEditClient, radio5GViewClient
from APIObject.wifi5GAPI import CHANNEL_API, BAND_WIDTH_API
from pages.SettingWirelessPage import WirelessRadioPage, CHANNEL_GUI, BAND_WITH_GUI
from base.WiFiLib import Wifi_lib
from base.SSHLib import SSH_Lib
from Config import config as cfg

@pytest.mark.usefixtures("login", "login_CAP_GUI", "create_shell")
class Test_radio5G_Edit():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60

        self.radio5GEditClt = radio5GEditClient()
        self.radio5GViewClt = radio5GViewClient()
        self.wrp = WirelessRadioPage(self.driver)
        self.client5G = Wifi_lib()
        self.session = SSH_Lib(SSHShell=self.SSHShell)

        self.channel_API_lst = ["auto", "36", "40", "44", "48", "52", "56", "60", "64", "100", "104", "112", "116",
                                "120", "124", "128", "132", "136", "140", "144", "149", "153", "157", "161", "165"]

        self.channel_GUI_exp = ["Auto", "36", "40", "44", "48", "52", "56", "60", "64", "100", "104", "112", "116",
                                "120", "124", "128", "132", "136", "140", "144", "149", "153", "157", "161", "165"]

        self.bandWith = BAND_WIDTH_API.B_20

    def test_RADIO24G_EDIT_CHANNEL_1(self):
        resBody_lst = []
        channelGUI_actual_lst = []
        channelDriver_actual_lst = []

        for item in self.channel_API_lst:
            # Setting Channel via API
            pload = self.radio5GEditClt.Create_Radio5GEdit_Pload(channel=item, bandW=self.bandWith)
            resBodyApply = self.radio5GEditClt.radio5GEdit(self.cookie, pload=pload).body

            # Wait 60s to apply configuration
            time.sleep(self.timeOut)

            # Getting Channel via Radio 5G View
            resBody = self.radio5GViewClt.radio5GView(self.cookie).body
            resBody_lst.append(resBody)

            # Getting Channel from driver
            channel = self.session.get_channel(cfg.WIFI_INT_5G)
            if item == 'auto':
                channel = 'auto'
            channelDriver_actual_lst.append(channel)

            # Getting Channel via WebGui
            self.wrp.navigate_to_radio_5G_setting_page()
            channelGUI = self.wrp.get_Channel5G_sp()
            channelGUI_actual_lst.append(channelGUI)
            # Click to tab Radio 5G again
            # self.wrp.click_Radio5G()

        # Verify the result Get from API
        self.radio5GViewClt.assert_result_lst(resBody_lst,
                                       channelLst=self.channel_API_lst)

        # Verify the result Get from GUI
        self.radio5GViewClt.assert_val_lst(self.channel_GUI_exp, channelGUI_actual_lst)

        # Verify the result Get from Driver
        self.radio5GViewClt.assert_val_lst(self.channel_API_lst, channelDriver_actual_lst)
