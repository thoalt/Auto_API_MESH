import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient


@pytest.mark.usefixtures("create_shell")
class Test_OpenSession():

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        ### Data Test
        self.data = ["openSession122144124141241241241"]
        self.exp = {"code": 8, "msg": "Invalid Action"}

        session = SSH_Lib(SSHShell=self.SSHShell)
        session.start_mobile_agent()
        self.client = openssesionClient()

    def test_OPEN_ACT_5(self):
        resBodyLst = []
        for actionName in self.data:
            payload = self.client.Create_OpenSession_Pload(action=actionName)
            reqID, res = self.client.Open_Session(pload=payload)
            resBody = res.body
            resBodyLst.append(resBody)
        self.client.assert_opensession_List(resBodyLst, self.exp['code'], self.exp['msg'])
