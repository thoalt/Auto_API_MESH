import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient
from Utilities import Utility as utl
from Config import config as cfg

@pytest.mark.usefixtures("create_shell")
class Test_OpenSession():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        ### Data Test
        self.data = []
        self.exp = {"code": 14, "msg": "Open Session Failed"}
        session = SSH_Lib(SSHShell=self.SSHShell)
        session.start_mobile_agent()
        self.client = openssesionClient()

    def test_OPEN_AUTH_2(self):
        clientMAC1 = "00:0E:C6:59:A1:A7"
        md5 = utl.md5_encrypt(cfg.STR_ENCRYPT + clientMAC1, cfg.SALT)
        payload = self.client.Create_OpenSession_Pload(authen=md5)
        reqID, res = self.client.Open_Session(pload=payload)
        resBody = res.body
        self.client.assert_opensession(resBody, self.exp['code'], self.exp['msg'])
