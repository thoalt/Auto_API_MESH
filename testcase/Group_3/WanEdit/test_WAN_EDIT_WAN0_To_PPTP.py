import time
import pytest
from APIObject.wanAPI import WanCreateEditClient, WAN_TYPE, IP_VER
from APIObject.wanAPI import WanRemoveClient, WanViewConfigClient
from pages.SettingWANPage import SettingWANPage


@pytest.mark.usefixtures("login", "login_CAP_GUI")
class Test_Wan_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success"}
        self.idx = 1
        self.vlanID = 10
        self.wanTypeAfter = WAN_TYPE().PPTP
        self.ipVerAfter = IP_VER().IPv4
        self.vlanIDAfter = 100

        self.userName_PPPoE = "User_PPPoE_Test"
        self.passW_PPPoE = "Pass_PPPoE_Test"

        self.serverPPTP = "10.10.10.10"
        self.userName_PPTP = "User_PPTP_Test"
        self.passW_PPTP = "Pass_PPTP_Test"

        self.serverL2TP = "99.99.99.99"
        self.userName_L2TP = "User_L2TP_Test"
        self.passW_L2TP = "Pass_PPTP_Test"

        self.ipAddr = "10.10.10.10"
        self.ipNetmask = "255.255.255.0"
        self.GW = "10.10.10.1"

        self.ipv6Addr = "fe80:0:0:0:200:4cff:fe43:172f"
        self.ipv6GW = "fe80:0:0:0:200:4cff:fe43:1"
        self.ipv6Type = "Auto"
        self.defaultRoute = True

        self.wanRemoveClt = WanRemoveClient()
        self.wanRemoveClt.Remove_All_WAN(self.cookie)

        self.wanEditClt = WanCreateEditClient()
        self.wanViewClt = WanViewConfigClient()
        self.wanViewClt.wanViewConfig(self.cookie)
        self.wp = SettingWANPage(self.driver)

    def test_WAN_EDIT_RES_1(self):
        time.sleep(self.timeOut)
        ploadCom = self.wanEditClt.Create_WanEdit_Common_Pload(
            wanIdx=0,
            wanType=self.wanTypeAfter
        )
        pload = self.wanEditClt.Create_WanCreate_Edit_WAN_PPTP(
            pload=ploadCom,
            server=self.serverPPTP,
            userName=self.userName_PPTP,
            pword=self.passW_PPTP)

        resBody = self.wanEditClt.wanCreateEdit(self.cookie, pload=pload).body
        self.wanEditClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
        time.sleep(30)
        resBody = self.wanViewClt.wanViewConfig(self.cookie).body
        self.wanViewClt.assert_result_WAN0(resBody,
                                      self.wanTypeAfter,
                                      server=self.serverPPTP,
                                      userName=self.userName_PPTP,
                                      passW=self.passW_PPTP)

        # Get Infor in GUI
        self.wp.navigate_to_WAN_setting_page()
        wanTypeGUI = self.wanViewClt.convert_wantype_API_to_GUI(self.wanTypeAfter)

        self.wanViewClt.assert_val(str(wanTypeGUI), str(self.wp.get_service()))
        self.wanViewClt.assert_val(self.serverPPTP, self.wp.get_Input_Server())
        self.wanViewClt.assert_val(self.userName_PPTP, self.wp.get_Input_User())
        self.wanViewClt.assert_val(self.passW_PPTP, self.wp.get_Input_Password())