import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient


@pytest.mark.usefixtures("create_shell")
class Test_OpenSession():

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        ### Data Test
        self.exp = {"code": 9, "msg": "Miss Request ID"}
        session = SSH_Lib(SSHShell=self.SSHShell)
        session.start_mobile_agent()
        self.client = openssesionClient()
        pload = self.client.Create_OpenSession_Pload()
        self.data = self.client.Remove_Request_ID_In_Pload(pload)

    def test_OPEN_ACT_2(self):
        resBodyLst = []
        for item in self.data:
            reqID, res = self.client.Open_Session(pload=item)
            resBody = res.body
            resBodyLst.append(resBody)
        self.client.assert_opensession_List(resBodyLst, self.exp['code'], self.exp['msg'])
