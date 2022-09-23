import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient


@pytest.mark.usefixtures("create_shell")
class Test_OpenSession():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        session = SSH_Lib(SSHShell=self.SSHShell)
        session.start_mobile_agent()
        self.client = openssesionClient()

    @pytest.mark.success
    def test_OPEN_TIME_1(self):
        reqID, res = self.client.Open_Session()
        resBody = res.body
        self.client.assert_opensession(resBody, 0, "Success")
