import time
import pytest
from APIObject.addNewNode import addNewNodeClient


@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ['addNewNode1', 'addNewNod', 'AddNewNode', 'ADDNEWNODE','Addnewnode' ,'addnewnode' ,'',
                     'addNewNode122144124141241241241']

        self.addNodeClt = addNewNodeClient()


    def test_TOPO_ADD_NEWNODE_1(self):
        resBody_lst = []
        for item in self.data:
            time.sleep(self.timeOut)
            pload = self.addNodeClt.Create_addNewNode_Pload(action=item)
            resBody = self.addNodeClt.addNewNode(self.cookie, pload).body
            resBody_lst.append(resBody)
        self.addNodeClt.assert_response_list(resBody_lst,
                                        self.exp['code'],
                                        self.exp['msg'])