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
        Create 2 wan PPPoE:
        - wan1: PPPoE, default Route = True
        - wan2: PPPoE, default Route = False
        - Edit wan2, từ default route = False thành default route = TRUE
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
                    wanType=WAN_TYPE().PPPoE
                )

                pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_PPPoE(
                    pload=ploadCom,
                    vlanID=self.vlanID + idx,
                    IPVer=self.IPVer,
                    dftRoute=False,
                    userName=self.userName + "_" + str(idx),
                    passW=self.passW + "_" + str(idx)
                )
                pload_Lst.append(pload)

        for item in pload_Lst:
            resBody = self.wanCreateClt.wanCreateEdit(self.cookie, pload=item).body
            self.wanCreateClt.assert_response(resBody,
                                            self.exp['code'],
                                            self.exp['msg'])
            time.sleep(30)

        ploadCom = self.wanCreateClt.Create_WanEdit_Common_Pload(
            wanIdx=2,
            wanType=WAN_TYPE().PPPoE
        )
        pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_PPPoE(
            pload=ploadCom,
            vlanID=self.vlanID + 5,
            IPVer=self.IPVer,
            userName=self.userName + "_" + str(0),
            passW=self.passW + "_" + str(0),
            dftRoute=True
        )

        resBody = self.wanCreateClt.wanCreateEdit(self.cookie, pload=pload).body
        self.wanCreateClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
        resBody = self.wanViewClt.wanViewConfig(self.cookie).body
