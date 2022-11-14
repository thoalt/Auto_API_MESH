import time
import pytest
from APIObject.addNewNode import addNewNodeClient
from Utilities import Utility as ult

@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 10, "msg": "Miss Attribute"}
        self.addNodeClt = addNewNodeClient()
        pload = self.addNodeClt.Create_addNewNode_Pload()
        self.data = [self.addNodeClt.Remove_Key_In_Pload(pload, 'action')]



    def test_TOPO_ADD_NEWNODE_1(self):
        resBody_lst = []
        for item in self.data:
            time.sleep(self.timeOut)
            resBody = self.addNodeClt.addNewNode(self.cookie, item).body
            resBody_lst.append(resBody)
        self.addNodeClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])