import time
import pytest
from APIObject.meshAPI import meshCreateClient, MESH_MODE, AUTHEN_MODE
from Utilities import Utility as utl

@pytest.mark.usefixtures("login")
class Test_Mesh_Create():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 10
        self.exp = {"code": 0, "msg": "Success"}
        self.meshCreateClt = meshCreateClient()
        self.mode = MESH_MODE.ROUTER
        self.ssidName = "ThoaTest_0"
        self.password = "1234567890_0"

    def test_WAN_CREATE_RES_1(self):
        time.sleep(self.timeOut)
        pload = self.meshCreateClt.Create_meshCreate_Pload(meshMode=self.mode,
                                                           ssidName=self.ssidName,
                                                           passW=self.password)

        resBody = self.meshCreateClt.meshCreate(self.cookie, pload=pload).body
        self.meshCreateClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])