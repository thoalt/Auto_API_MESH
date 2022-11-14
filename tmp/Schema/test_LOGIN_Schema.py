import time
import pytest
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from Config import Schema_Template as scTmp


class Test_Schema_Opensession():
    """
    Description: Verify Schema for APIs of LAN page:
        - lanView
    """

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        # Call API Lanview
        self.ClientSes = openssesionClient()
        self.cookie = self.ClientSes.Open_Sesion_And_Get_Cookie()
        self.loginClt = LoginClient()

    def test_LanView_Schema(self):
        time.sleep(self.timeOut)
        resBody = self.loginClt.login(cookies=self.cookie).body

        self.ClientSes.valid_schema_common(resBody, schema=scTmp.schema_dataNull_common)

