import time
import pytest
from APIObject.addNewNode import addNewNodeClient
from Config import Schema_Template as scTmp

@pytest.mark.usefixtures("login")
class Test_Topology():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.addClt = addNewNodeClient()

    def test_Topology_Schema(self):
        time.sleep(self.timeOut)
        resBody = self.addClt.addNewNode(self.cookie).body

        self.addClt.valid_schema_common(resBody, schema=scTmp.schema_addNewNode)

