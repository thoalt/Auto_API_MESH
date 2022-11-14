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
        self.wanType = WAN_TYPE().STATIC
        self.vlanID = 10
        self.IPVer = IP_VER().IPv6
        self.ipv6Addr = "fe80:0:0:0:200:4cff:fe43:172f"
        self.ipv6GW = "fe80:0:0:0:200:4cff:fe43:1"
        self.ipv6Type = "Auto"
        self.defaultRoute = True

        self.wanEditClt = WanCreateEditClient()
        self.wanEditClt.Create_DHCP_Dual(cookies=self.cookie,
                                         index=1,
                                         vlanId=99)

        time.sleep(30)
        self.wanEditClt.Create_DHCP_IPv4(cookies=self.cookie,
                                         index=2,
                                         vlanId=999)

        self.wanViewClt.wanViewConfig(self.cookie)
        self.wp = SettingWANPage(self.driver)

    def test_WAN_CREATE_RES_1(self):
        time.sleep(self.timeOut)
        ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
            wanIdx=self.wanIdx,
            wanType=self.wanType
        )
        pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_IPV6_pload(
            pload=ploadCom,
            vlanID=self.vlanID,
            IPVer=self.IPVer,
            IPV6Addr=self.ipv6Addr,
            IPV6GW=self.ipv6GW,
            ipv6Type=self.ipv6Type
        )

        resBody = self.wanCreateClt.wanCreateEdit(self.cookie, pload=pload).body
        self.wanCreateClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
        time.sleep(30)
        resBody = self.wanViewClt.wanViewConfig(self.cookie).body
        self.wanViewClt.assert_result_WAN3(resBody,
                                      self.wanType,
                                      self.vlanID,
                                      self.IPVer,
                                      IPV6Addr=self.ipv6Addr,
                                      IPV6GW=self.ipv6GW,
                                      ipv6Type=self.ipv6Type)

        # GUI Setting
        self.wp.navigate_to_WAN_3_setting_page()
        wanTypeGUI = self.wanViewClt.convert_wantype_API_to_GUI(self.wanType)
        self.wanViewClt.assert_val(str(wanTypeGUI), str(self.wp.get_service()))
        self.wanViewClt.assert_val(int(self.vlanID), int(self.wp.get_VLAN_ID()))
        self.wanViewClt.assert_val(self.IPVer, self.wp.get_IPVersion())

        self.wanViewClt.assert_val(self.ipv6Addr, self.wp.get_IPV6_Addr())
        self.wanViewClt.assert_val(self.ipv6GW, self.wp.get_IPV6_Gateway())