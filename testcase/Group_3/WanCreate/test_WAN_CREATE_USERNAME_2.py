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
        self.exp = {"code": 11, "msg": "Verify Fail"}
        self.wanCreateClt = WanCreateEditClient()
        self.wanViewClt = WanViewConfigClient()
        self.wanRemoveClt = WanRemoveClient()
        self.wanRemoveClt.Remove_All_WAN(cookies=self.cookie)

        self.wanIdx = 1
        self.wanType = WAN_TYPE().PPPoE
        self.vlanID = 10
        self.IPVer = IP_VER().DUAL
        self.defRoute = True

        self.userName = ["aá1", "aà2", "aã3", "aạ4 aă1", "aắ2", "aằ3", "aặ4", "aẵ5", "aâ1", "aấ2", "aầ3", "aẫ4", "aậ5",
                         "eé1", "eè2", "eẽ3", "eẹ4", "eê1", "eế2", "eề3", "eễ4", "eệ5", "oô1", "oố2", "oồ3", "oỗ4",
                         "oộ5", "oơ1", "oớ2", "oờ3", "oỡ4", "oợ5", "uư1", "uứ2", "uừ3", "uữ4", "uự5"]

        self.passW = "PassPPPoE"
        self.wp = SettingWANPage(self.driver)

    def test_WAN_CREATE_RES_1(self):
        time.sleep(self.timeOut)
        for item in self.userName:
            ploadCom = self.wanCreateClt.Create_WanCreate_Common_Pload(
                wanIdx=self.wanIdx,
                wanType=self.wanType
            )
            pload = self.wanCreateClt.Create_WanCreate_Edit_WAN_PPPoE(
                pload=ploadCom,
                vlanID=self.vlanID,
                IPVer=self.IPVer,
                userName=item,
                passW=self.passW,
                dftRoute=self.defRoute
            )

            resBody = self.wanCreateClt.wanCreateEdit(self.cookie, pload=pload).body
            self.wanCreateClt.assert_response(resBody,
                                            self.exp['code'],
                                            self.exp['msg'])
            time.sleep(2)
