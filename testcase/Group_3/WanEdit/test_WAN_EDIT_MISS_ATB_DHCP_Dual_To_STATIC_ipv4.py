import time
import pytest
from APIObject.wanAPI import WanCreateEditClient, WAN_TYPE, IP_VER
from APIObject.wanAPI import WanRemoveClient, WanViewConfigClient

@pytest.mark.usefixtures("login")
class Test_Wan_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 10, "msg": "Miss Attribute"}
        self.idx = 1
        self.vlanID = 10
        self.wanTypeAfter = WAN_TYPE().STATIC
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
        self.wanEditClt.Create_DHCP_Dual(cookies=self.cookie,
                                         index=self.idx,
                                         vlanId=self.vlanID)

        self.wanViewClt = WanViewConfigClient()
        self.wanViewClt.wanViewConfig(self.cookie)

    def test_WAN_EDIT_RES_1(self):
        time.sleep(self.timeOut)
        ploadCom = self.wanEditClt.Create_WanEdit_Common_Pload(
            wanIdx=self.idx,
            wanType=self.wanTypeAfter
        )
        pload = self.wanEditClt.Create_WanCreate_Edit_WAN_IPV4_pload(
            pload=ploadCom,
            vlanID=self.vlanIDAfter,
            IPVer=self.ipVerAfter,
            IPV4Addr=self.ipAddr,
            IPV4Net=self.ipNetmask,
            IPV4GW=self.GW
        )
        ploadList = self.wanEditClt.Remove_Attribute_Without_Action_RequestID(pload)

        resBody_Respone_lst = []
        resBody_Result_lst = []

        for item in ploadList:
            resBodyRespone = self.wanEditClt.wanCreateEdit(self.cookie, pload=item).body

            resBody_Respone_lst.append(resBodyRespone)
            time.sleep(5)
        #     resBody = self.wanViewClt.wanViewConfig(self.cookie).body
        #     resBody_Result_lst.append(resBody)
        #
        # self.wanEditClt.assert_response_list(resBody_Respone_lst,
        #                                 self.exp['code'],
        #                                 self.exp['msg'])
        # self.wanViewClt.assert_result_list(resBody_Result_lst,
        #                               self.wanTypeAfter,
        #                               self.vlanIDAfter,
        #                               self.ipVerAfter,
        #                               IPV4Addr=self.ipAddr,
        #                               IPV4Net=self.ipNetmask,
        #                               IPV4GW=self.GW)