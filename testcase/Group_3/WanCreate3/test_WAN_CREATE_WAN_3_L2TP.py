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
        self.wanCreateClt = WanCreateEditClient()
        self.wanViewClt = WanViewConfigClient()
        self.wanRemoveClt = WanRemoveClient()
        self.wanRemoveClt.Remove_All_WAN(cookies=self.cookie)

        self.wanIdx = 3
        self.wanType = WAN_TYPE().L2TP
        self.vlanID = 10

        self.userName = "UserL2TP"
        self.passW = "PassL2TP"
        self.server = "100.100.100.100"

        self.wp = SettingWANPage(self.driver)
        self.wanEditClt = WanCreateEditClient()
        self.wanEditClt.Create_DHCP_Dual(cookies=self.cookie,
                                         index=1,
                                         vlanId=99)

        time.sleep(30)
        self.wp.refresh()
        self.wanEditClt.Create_DHCP_IPv4(cookies=self.cookie,
                                         index=2,
                                         vlanId=999)
        time.sleep(30)
        self.wp.refresh()

        self.wanViewClt.wanViewConfig(self.cookie)

    def test_WAN_CREATE_RES_1(self):
        time.sleep(self.timeOut)
        ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
            wanIdx=self.wanIdx,
            wanType=self.wanType
        )

        pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_L2TP(
            pload=ploadCom,
            server=self.server,
            userName=self.userName,
            pword=self.passW
        )

        resBody = self.wanCreateClt.wanCreateEdit(self.cookie, pload=pload).body
        self.wanCreateClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
        time.sleep(30)
        resBody = self.wanViewClt.wanViewConfig(self.cookie).body

        self.wanViewClt.assert_result_WAN3(resBody,
                                      self.wanType,
                                      server=self.server,
                                      userName=self.userName,
                                      passW=self.passW)

        # Get Infor in GUI
        self.wp.navigate_to_WAN_3_setting_page()
        wanTypeGUI = self.wanViewClt.convert_wantype_API_to_GUI(self.wanType)

        self.wanViewClt.assert_val(str(wanTypeGUI), str(self.wp.get_service()))
        self.wanViewClt.assert_val(self.server, self.wp.get_Input_Server())
        self.wanViewClt.assert_val(self.userName, self.wp.get_Input_User())
        self.wanViewClt.assert_val(self.passW, self.wp.get_Input_Password())
