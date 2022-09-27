import time
import pytest
from APIObject.wifi24GAPI import radio24GViewClient
from pages.SettingWirelessPage import WirelessRadioPage


@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_Radio2GView():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 60
        self.exp = {"code": 0, "msg": "Success", "action": "radio2.4GView"}
        self.dataLst = ["20 MHz", "20/40 MHz"]
        self.dataExp = ["20MHz", "20/40MHz"]
        self.radio2G = radio24GViewClient()

        self.wrp = WirelessRadioPage(self.driver)
        self.wrp.navigate_to_radio_2G_page()

    @pytest.mark.success
    def test_RADIO_2G_ACT_1(self):
        resBody_lst = []
        for data in self.dataLst:
            self.wrp.click_Btn_Edit_Radio2G()
            self.wrp.setting_Radio(bandW='2G', bandwith=data, clickApply=True)
            time.sleep(self.timeOut)

            # Run API Radio view
            resBody = self.radio2G.radio24GView(self.cookie).body
            resBody_lst.append(resBody)

        self.radio2G.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

        self.radio2G.assert_result_lst(resBody_lst,
                                       bandWLst=self.dataExp)