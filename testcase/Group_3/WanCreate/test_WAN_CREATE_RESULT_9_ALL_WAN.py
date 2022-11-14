import time
import pytest
from APIObject.wanAPI import WanCreateEditClient, WAN_TYPE, IP_VER
from APIObject.wanAPI import WanRemoveClient, WanViewConfigClient

@pytest.mark.usefixtures("login")
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
        self.wanType = WAN_TYPE().PPTP
        self.vlanID = 10
        self.IPVer = IP_VER().DUAL

        self.userName = "User_Test"
        self.passW = "Pass_Test"

        self.serverPPTP = "10.10.10.10"
        self.serverL2TP = "99.99.99.99"

        self.ipAddr = "10.10.10.10"
        self.ipNetmask = "255.255.255.0"
        self.GW = "10.10.10.1"

        self.ipv6Addr = "fe80:0:0:0:200:4cff:fe43:172f"
        self.ipv6GW = "fe80:0:0:0:200:4cff:fe43:1"
        self.ipv6Type = "Auto"
        self.defaultRoute = True

    def test_WAN_CREATE_RES_1(self):
        """Description:
        wan1: pppoE_Dual
        wan2: STATIC_DUAL
        wan3: DHCP_DUAL
        """
        time.sleep(self.timeOut)
        pload_Lst = []
        for idx in range(1, 4):
            if idx == 1:
                ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
                    wanIdx=idx,
                    wanType=WAN_TYPE().PPPoE
                )

                pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_PPPoE(
                    pload=ploadCom,
                    vlanID=self.vlanID + idx,
                    IPVer=self.IPVer,
                    dftRoute=self.defaultRoute,
                    userName=self.userName + "_" + str(idx),
                    passW=self.passW + "_" + str(idx)
                )
                pload_Lst.append(pload)

            elif idx == 2:
                ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
                    wanIdx=idx,
                    wanType=WAN_TYPE().STATIC
                )

                pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_Dual_pload(
                    pload=ploadCom,
                    vlanID=self.vlanID + idx,
                    IPVer=IP_VER.DUAL,
                    IPV4Addr=self.ipAddr,
                    IPV4Net=self.ipNetmask,
                    IPV4GW=self.GW,
                    IPV6Addr=self.ipv6Addr,
                    IPV6GW=self.ipv6GW,
                    ipv6Type=self.ipv6Type,
                    dftRoute=self.defaultRoute
                )

                pload_Lst.append(pload)

            elif idx == 3:
                ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
                    wanIdx=idx,
                    wanType=WAN_TYPE().DHCP
                )

                pload = self.wanCreateClt.Create_WanCreate_Edit_DHCP_pload(
                    pload=ploadCom,
                    vlanID=self.vlanID + idx,
                    IPVer=IP_VER.DUAL
                )
                pload_Lst.append(pload)

        for item in pload_Lst:
            resBody = self.wanCreateClt.wanCreateEdit(self.cookie, pload=item).body
            self.wanCreateClt.assert_response(resBody,
                                            self.exp['code'],
                                            self.exp['msg'])
            time.sleep(30)


        resBody = self.wanViewClt.wanViewConfig(self.cookie).body

        ## Check full item
        self.wanViewClt.assert_val(4, len(resBody))