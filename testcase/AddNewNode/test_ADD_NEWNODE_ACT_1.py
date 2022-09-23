import time
import pytest
from APIObject.addNewNode import addNewNodeClient


@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 5
        self.exp = {"code": 0, "msg": "Success", "action": "addNewNode"}
        self.addNodeClt = addNewNodeClient()

    @pytest.mark.success
    def test_TOPO_ACT_1(self):
        time.sleep(self.timeOut)
        resBody = self.addNodeClt.addNewNode(self.cookie).body
        self.addNodeClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'],
                                        self.exp['action'])