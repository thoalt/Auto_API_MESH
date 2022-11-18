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

        self.wanIdx = 1
        self.wanType = WAN_TYPE().STATIC
        self.vlanID = 10
        self.IPVer = IP_VER().DUAL

        self.ipAddr = "10.10.10.10"
        self.ipNetmask = "255.255.255.0"
        self.GW = "10.10.10.1"

        self.ipv6Addr = "fe80:0:0:0:200:4cff:fe43:172f"
        self.ipv6GW = "fe80:0:0:0:200:4cff:fe43:1"
        self.ipv6Type = "Auto"
        self.defaultRoute = True
        self.wp = SettingWANPage(self.driver)

    def test_WAN_CREATE_RES_1(self):
        time.sleep(self.timeOut)
        ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
            wanIdx=self.wanIdx,
            wanType=self.wanType
        )
        pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_Dual_pload(
            pload=ploadCom,
            vlanID=self.vlanID,
            IPVer=self.IPVer,
            IPV4Addr=self.ipAddr,
            IPV4Net=self.ipNetmask,
            IPV4GW=self.GW,
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
        self.wanViewClt.assert_result_WAN1(resBody,
                                           self.wanType,
                                           self.vlanID,
                                           self.IPVer,
                                           IPV4Addr=self.ipAddr,
                                           IPV4Net=self.ipNetmask,
                                           IPV4GW=self.GW,
                                           IPV6Addr=self.ipv6Addr,
                                           IPV6GW=self.ipv6GW)

        # GUI Setting
        self.wp.navigate_to_WAN_1_setting_page()
        wanTypeGUI = self.wanViewClt.convert_wantype_API_to_GUI(self.wanType)
        ipVerGui = self.wanViewClt.conver_IPVer_API_To_GUI(self.IPVer)

        self.wanViewClt.assert_val(str(wanTypeGUI), str(self.wp.get_service()))
        self.wanViewClt.assert_val(int(self.vlanID), int(self.wp.get_VLAN_ID()))
        self.wanViewClt.assert_val(ipVerGui, self.wp.get_IPVersion())

        self.wanViewClt.assert_val(self.ipAddr, self.wp.get_IPV4_Addr())
        self.wanViewClt.assert_val(self.ipNetmask, self.wp.get_IPV4_Netmask())
        self.wanViewClt.assert_val(self.GW, self.wp.get_IPV4_Gateway())

        self.wanViewClt.assert_val(self.ipv6Addr, self.wp.get_IPV6_Addr())
        self.wanViewClt.assert_val(self.ipv6GW, self.wp.get_IPV6_Gateway())

