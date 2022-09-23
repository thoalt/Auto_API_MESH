import time

import pytest
from assertpy import assert_that
from base.SSHLib import SSH_Lib
from APIObject.openssesion import openssesionClient


@pytest.mark.usefixtures("create_shell")
class Test_OpenSession():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.data = [5]
        session = SSH_Lib(SSHShell=self.SSHShell)
        session.start_mobile_agent()
        self.client = openssesionClient()


    def test_OPEN_TIME_3(self):
        # Open session first time
        reqID, res = self.client.Open_Session()
        resBody = res.body
        sesID1, salt = self.client.Get_SessionID(res.headers)
        self.client.assert_opensession(resBody, 0, "Success")
        time.sleep(self.data[0])

        # Open session second time
        reqID, res = self.client.Open_Session()
        self.client.assert_opensession(resBody, 0, "Success")
        sesID2, salt = self.client.Get_SessionID(res.headers)
        self.client.assert_same_sesionID(sesID1, sesID2)