import time
import pytest
from APIObject.wanAPI import WanViewConfigClient
from Config import Schema_Template as scTmp


@pytest.mark.usefixtures("login")
class Test_Schema_For_WAN():
    """
    Description: Verify Schema for APIs of LAN page:
        - lanView
    """

    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        # Call API Lanview
        self.WanviewClt = WanViewConfigClient()

    def test_LanView_Schema(self):
        time.sleep(self.timeOut)
        response = self.WanviewClt.wanViewConfig(self.cookie)
        resBody = response.body

        self.WanviewClt.valid_schema_common(resBody)
        self.WanviewClt.valid_schema_resul(resBody, schema=scTmp.schema_wanViewConfig_IPoE_Dynamic_result, require_all=False)

