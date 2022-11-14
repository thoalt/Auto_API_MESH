import time
import pytest
from APIObject.lanAPI import LanViewClient
from pages.SettingLANPage import SettingLANPage

@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_LanView():

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 90
        self.exp = {"code": 0, "msg": "Success", "action": "lanView"}
        self.dataLst = ["255.255.255.0", "255.255.0.0", "255.0.0.0"]

        # Call API Lanview
        self.LanviewClt = LanViewClient()

        # Call Setting LanPage
        self.slp = SettingLANPage(self.driver)


    def test_LANVIEW_RESULT_1(self):
        resBody_lst = []
        for data in self.dataLst:
            # Setting Netmask
            self.slp.navigate_to_LAN_Setting_tab()
            self.slp.set_LAN_value(netMask=data, clickApply=True)
            time.sleep(self.timeOut)

            # Post API lanview
            resBody = self.LanviewClt.lanView(self.cookie).body
            resBody_lst.append(resBody)

        self.LanviewClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])

        self.LanviewClt.assert_result_lst(resBody_lst,
                                         netMask_Lst=self.dataLst)