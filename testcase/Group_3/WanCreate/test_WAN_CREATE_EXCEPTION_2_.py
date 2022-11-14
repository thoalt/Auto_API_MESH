import time
import pytest
from APIObject.wanAPI import WanCreateEditClient, WAN_TYPE, IP_VER
from APIObject.wanAPI import WanRemoveClient, WanViewConfigClient

@pytest.mark.usefixtures("login")
class Test_Wan_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.wanCreateClt = WanCreateEditClient()
        self.wanViewClt = WanViewConfigClient()
        self.wanRemoveClt = WanRemoveClient()
        self.wanRemoveClt.Remove_All_WAN(cookies=self.cookie)

        self.wanIdx = 1
        self.wanType = WAN_TYPE().PPTP
        self.vlanID = 10


        self.IPVer = IP_VER().DUAL
        self.defaultRoute = True

        self.userName = "User_Test"
        self.passW = "Pass_Test"

        self.serverPPTP = "10.10.10.10"
        self.serverL2TP = "99.99.99.99"

    def test_WAN_CREATE_RES_1(self):
        """Description:
        wan1: PPTP
        wan2: L2TP
        wan3: pppoE_Dual
        wan4: DHCP_DUAL
        """
        time.sleep(self.timeOut)
        pload_Lst = []
        for idx in range(1, 5):
            if idx == 1:
                ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
                    wanIdx=idx,
                    wanType=WAN_TYPE().PPTP
                )

                pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_PPTP(
                    pload=ploadCom,
                    server=self.serverPPTP,
                    userName=self.userName + "_" + str(idx),
                    pword=self.passW + "_" + str(idx)
                )
                pload_Lst.append(pload)

            elif idx == 2:
                ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
                    wanIdx=idx,
                    wanType=WAN_TYPE().L2TP
                )

                pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_L2TP(
                    pload=ploadCom,
                    server=self.serverL2TP,
                    userName=self.userName + "_" + str(idx),
                    pword=self.passW + "_" + str(idx)
                )
                pload_Lst.append(pload)

            elif idx == 3:
                ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
                    wanIdx=idx,
                    wanType=WAN_TYPE().PPPoE
                )

                pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_PPPoE(
                    pload=ploadCom,
                    vlanID=self.vlanID,
                    IPVer=self.IPVer,
                    userName=self.userName + "_" + str(idx),
                    passW=self.passW + "_" + str(idx),
                    dftRoute=self.defaultRoute
                )
                pload_Lst.append(pload)

            elif idx == 4:
                ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
                    wanIdx=3,
                    wanType=WAN_TYPE().DHCP
                )

                pload = self.wanCreateClt.Create_WanCreate_Edit_DHCP_pload(
                    pload=ploadCom,
                    vlanID=self.vlanID + idx,
                    IPVer=IP_VER.DUAL
                )
                pload_Lst.append(pload)

        for idx, item in enumerate(pload_Lst):
            resBody = self.wanCreateClt.wanCreateEdit(self.cookie, pload=item).body
            if idx == 3:
                self.wanCreateClt.assert_response(resBody,
                                            self.exp['code'],
                                            self.exp['msg'])
            time.sleep(30)


        resBody = self.wanViewClt.wanViewConfig(self.cookie).body

        ## Check full item
        self.wanViewClt.assert_val(4, len(resBody))