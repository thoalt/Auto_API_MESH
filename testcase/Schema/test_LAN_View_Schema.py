import time
import pytest
from APIObject.lanAPI import LanViewClient
from Config import Schema_Template as scTmp


@pytest.mark.usefixtures("login")
class Test_Schema_For_LAN():
    """
    Description: Verify Schema for APIs of LAN page:
        - lanView
    """

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        # Call API Lanview
        self.LanviewClt = LanViewClient()

    def test_LanView_Schema(self):
        time.sleep(self.timeOut)
        response = self.LanviewClt.lanView(self.cookie)
        resBody = response.body

        self.LanviewClt.valid_schema_common(resBody)
        self.LanviewClt.valid_schema_resul(resBody, schema=scTmp.schema_lanView_result)

