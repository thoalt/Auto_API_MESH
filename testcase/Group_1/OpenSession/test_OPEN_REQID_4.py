import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient


@pytest.mark.usefixtures("create_shell")
class Test_OpenSession():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.data = [1.12]
        self.exp = {"code": 11, "msg": "Verify Fail"}
        session = SSH_Lib(SSHShell=self.SSHShell)
        session.start_mobile_agent()
        self.client = openssesionClient()

    def test_OPEN_REQID_4(self):
        resBodyLst = []
        for reqID in self.data:
            payload = self.client.Create_OpenSession_Pload(reqID=reqID)
            reqID, res = self.client.Open_Session(pload=payload)
            resBody = res.body
            resBodyLst.append(resBody)
        self.client.assert_opensession_List(resBodyLst, self.exp['code'], self.exp['msg'])
