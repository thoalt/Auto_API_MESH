import time
import pytest
from APIObject.wanAPI import WanCreateEditClient, WAN_TYPE, IP_VER
from pages.SettingWANPage import SettingWANPage

@pytest.mark.usefixtures("login")
class Test_Wan_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success"}
        self.wanCreateClt = WanCreateEditClient()
        self.wanpg = SettingWANPage()

    def test_WAN_CREATE_RES_1(self):
        time.sleep(self.timeOut)
        ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
            wanIdx=1,
            wanType=WAN_TYPE().DHCP
        )
        pload = self.wanCreateClt.Create_WanCreate_Edit_DHCP_pload(
            pload=ploadCom,
            vlanID= 10,
            IPVer=IP_VER().IPv4
        )

        resBody = self.wanCreateClt.wanCreateEdit(self.cookie, pload=pload).body

        self.wanpg.navigate_to_WAN_setting_page()
        self.wanCreateClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])