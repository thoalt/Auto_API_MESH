import time
import pytest
from APIObject.openssesion import openssesionClient
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
        self.OpenSS = openssesionClient()

    def test_LanView_Schema(self):
        time.sleep(self.timeOut)
        reqID, response = self.OpenSS.Open_Session()
        resBody = response.body

        self.OpenSS.valid_schema_common(resBody, schema=scTmp.schema_dataNull_common)

