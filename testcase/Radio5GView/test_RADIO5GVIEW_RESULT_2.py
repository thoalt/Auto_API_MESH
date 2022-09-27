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
        self.dataLst = ["Enable"]
        self.dataExp = [True]
        self.radio5G = radio5GViewClient()

        # self.wrp = WirelessRadioPage(self.driver)
        # self.wrp.navigate_to_radio_5G_page()

    def test_RADIO_5G_ACT_1(self):
        resBody_lst = []
        for data in self.dataLst:
            # self.wrp.click_Btn_Edit_Radio2G()
            # self.wrp.setting_Radio(bandW='2G', bandwith=data, clickApply=True)
            # time.sleep(self.timeOut)
            # Run API Radio view
            resBody = self.radio5G.radio5GView(self.cookie).body
            resBody_lst.append(resBody)

        self.radio5G.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

        self.radio5G.assert_result_lst(resBody_lst,
                                       enableLst=self.dataExp)