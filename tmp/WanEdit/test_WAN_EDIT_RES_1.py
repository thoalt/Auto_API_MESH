import time
import pytest
from APIObject.wanAPI import WanCreateEditClient, WAN_TYPE, IP_VER


@pytest.mark.usefixtures("login")
class Test_Wan_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success"}
        self.wanEditClt = WanCreateEditClient()


    def test_WAN_CREATE_RES_1(self):
        time.sleep(self.timeOut)
        ploadCom = self.wanEditClt.Create_WanCreate_Common_Pload(
            wanIdx=1,
            wanType=WAN_TYPE().DHCP
        )
        pload = self.wanEditClt.Create_WanCreate_Edit_DHCP_pload(
            pload=ploadCom,
            vlanID= 10,
            IPVer=IP_VER().IPv4
        )

        resBody = self.wanEditClt.wanCreateEdit(self.cookie, pload=pload).body
        self.wanEditClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])