import time
import pytest
from APIObject.wifi5GAPI import radio5GViewClient
from pages.SettingWirelessPage import WirelessRadioPage


@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_Radio5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 0, "msg": "Success", "action": "radio5GView"}
        self.dataLst = ["Auto", "36", "40", "44", "48", "52", "56", "60", "64", "100", "104", "112", "116", "120", "124", "128", "132", "136", "140", "144", "149", "153", "157", "161", "165"]
        self.dataExp = ["auto", "36", "40", "44", "48", "52", "56", "60", "64", "100", "104", "112", "116", "120", "124", "128", "132", "136", "140", "144", "149", "153", "157", "161", "165"]

        # self.dataLst = ["Auto", "36"]
        # self.dataExp = ["auto", "36"]

        self.radio5G = radio5GViewClient()

        self.wrp = WirelessRadioPage(self.driver)
        self.wrp.navigate_to_radio_5G_page()

    def test_RADIO_5G_ACT_1(self):
        resBody_lst = []
        for data in self.dataLst:
            self.wrp.click_Btn_Edit_Radio5G()

            self.wrp.setting_Radio(bandW='5G', standard='11ac', channel=data, clickApply=True)
            time.sleep(self.timeOut)

            # Click to tab Radio 5G again
            self.wrp.click_Radio5G()

            #Call API Radio view
            resBody = self.radio5G.radio5GView(self.cookie).body
            resBody_lst.append(resBody)


        self.radio5G.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

        self.radio5G.assert_result_lst(resBody_lst,
                                       channelLst=self.dataExp)