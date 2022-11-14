import time
import pytest
from APIObject.wanAPI import WanCreateEditClient, WAN_TYPE, IP_VER


@pytest.mark.usefixtures("login")
class Test_Wan_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success"}
        self.wanCreateClt = WanCreateEditClient()
        self.wanIdx = 1
        self.wanType = WAN_TYPE().DHCP
        self.vlanID = 10,
        self.IPVer = IP_VER().IPv4


    def test_WAN_CREATE_RES_1(self):
        time.sleep(self.timeOut)
        ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
            wanIdx=self,
            wanType=WAN_TYPE().DHCP
        )
        pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_IPV4_pload(
            pload=ploadCom,
            vlanID=self.vlanID,
            IPVer=IP_VER().DUAL
        )

        resBody = self.wanCreateClt.wanCreateEdit(self.cookie, pload=pload).body
        self.wanCreateClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])