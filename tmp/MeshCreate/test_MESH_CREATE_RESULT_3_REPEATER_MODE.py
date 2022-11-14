import time
import pytest
from APIObject.meshAPI import meshCreateClient, meshViewClient, MESH_MODE, AUTHEN_MODE
from Utilities import Utility as utl

@pytest.mark.usefixtures("login")
class Test_Mesh_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success"}
        self.meshCreateClt = meshCreateClient()
        self.meshViewClt = meshViewClient()

        self.mode = MESH_MODE.REPEATER
        self.ssidName = "ThoaTest_0"
        self.password = "1234567890_0"
        self.repeatDct = {
            "reSSID": "",
            "reAuthen": "",
            "rePass": ""
        }
    @pytest.mark.skip()
    def test_WAN_CREATE_RES_1(self):
        time.sleep(self.timeOut)

        # Create Mesh
        pload = self.meshCreateClt.Create_meshCreate_Pload(meshMode=self.mode,
                                                           ssidName=self.ssidName,
                                                           passW=self.password)

        pload = self.meshCreateClt.Create_meshCreate_Mode_Repeater_Pload(payload=pload,
                                                                         ReSsidName=self.repeatDct['reSSID'],
                                                                         ReAutheMode=self.repeatDct['reAuthen'],
                                                                         RePass=self.repeatDct['rePass'])

        resBody = self.meshCreateClt.meshCreate(self.cookie, pload=pload).body

        # View Mesh
        resBody = self.meshViewClt.meshView(self.cookie).body
        self.meshViewClt.assert_meshmode(resBody, expectMode=self.mode)
        self.meshViewClt.assert_repeater(resBody, repDict=self.repeatDct)