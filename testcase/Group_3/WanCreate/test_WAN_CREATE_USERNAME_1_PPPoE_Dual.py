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

        self.wanIdx = 1
        self.wanType = WAN_TYPE().PPPoE
        self.vlanID = 10
        self.IPVer = IP_VER().DUAL
        self.defRoute = True

        self.userName = ["e",
                        "5",
                        "%",
                        "?",
                        "`",
                        "t!",
                        "gh",
                        "3#",
                        "test@hec",
                        "uidwvgNleD1234567890`~!@#$%^*()_",
                        "uidwvgNleD1234567890-=+{[]}|;:<,",
                        "uidwvgNleD1234567890.>?/txblaudp"
                         ]

        self.passW =  ["e",
                        "5",
                        "%",
                        "?",
                        "`",
                        "t!",
                        "gh",
                        "3#",
                        "test@hec",
                        "uidwvgNleD1234567890`~!@#$%^*()_",
                        "uidwvgNleD1234567890-=+{[]}|;:<,",
                        "uidwvgNleD1234567890.>?/txblaudp"
                         ]
        self.wp = SettingWANPage(self.driver)

    def test_WAN_CREATE_RES_1(self):
        time.sleep(self.timeOut)
        for item in self.userName:
            self.wanRemoveClt.Remove_All_WAN(cookies=self.cookie)

            ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
                wanIdx=self.wanIdx,
                wanType=self.wanType
            )
            pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_PPPoE(
                pload=ploadCom,
                vlanID=self.vlanID,
                IPVer=self.IPVer,
                userName=item,
                passW=item,
                dftRoute=self.defRoute
            )

            resBody = self.wanCreateClt.wanCreateEdit(self.cookie, pload=pload).body
            self.wanCreateClt.assert_response(resBody,
                                            self.exp['code'],
                                            self.exp['msg'])
            time.sleep(45)
            resBody = self.wanViewClt.wanViewConfig(self.cookie).body

            self.wanViewClt.assert_result_WAN1(resBody,
                                               self.wanType,
                                               self.vlanID,
                                               self.IPVer,
                                               userName=item,
                                               passW=item)

            # Get Infor in GUI
            self.wp.navigate_to_WAN_1_setting_page()
            wanTypeGUI = self.wanViewClt.convert_wantype_API_to_GUI(self.wanType)
            ipVerGui = self.wanViewClt.conver_IPVer_API_To_GUI(self.IPVer)

            self.wanViewClt.assert_val(str(wanTypeGUI), str(self.wp.get_service()))
            self.wanViewClt.assert_val(int(self.vlanID), int(self.wp.get_VLAN_ID()))
            self.wanViewClt.assert_val(ipVerGui, self.wp.get_IPVersion())

            self.wanViewClt.assert_val(item, self.wp.get_PPPoE_IPV4_User())
            self.wanViewClt.assert_val(item, self.wp.get_PPPoE_IPV4_Pass())
            self.wanViewClt.assert_val(self.defRoute, self.wp.get_default_route())
