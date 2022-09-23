import time
import pytest
from APIObject.radio5GView import radio5GViewClient
from pages.SettingWirelessPage import WirelessRadioPage


@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_Radio5GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 0, "msg": "Success", "action": "radio5GView"}
        self.dataLst = ["20 MHz", "40 MHz", "80 MHz"]
        self.dataExp = ["20MHz", "40MHz", "80MHz"]

        self.radio5G = radio5GViewClient()

        self.wrp = WirelessRadioPage(self.driver)
        self.wrp.navigate_to_radio_5G_page()

    def test_RADIO_5G_ACT_1(self):
        resBody_lst = []
        for data in self.dataLst:
            self.wrp.click_Btn_Edit_Radio5G()

            self.wrp.setting_Radio(bandW='5G', standard='11ac', bandwith=data, clickApply=True)
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
                                       bandWLst=self.dataExp)