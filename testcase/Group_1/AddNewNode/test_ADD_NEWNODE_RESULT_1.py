import time
import pytest
from APIObject.addNewNode import addNewNodeClient
from APIObject.networkinfoView import networkinfoViewClient

@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success"}
        self.addNodeClt = addNewNodeClient()
        self.network = networkinfoViewClient()

    @pytest.mark.skip(reason="This is Manual Testcase")
    def test_TOPO_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.addNodeClt.addNewNode(self.cookie).body
        time.sleep(240)
        self.addNodeClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])
