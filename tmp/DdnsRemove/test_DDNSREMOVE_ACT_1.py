import time
import pytest
from APIObject.serviceAPI import ddnsRemoveClient

@pytest.mark.usefixtures("login")
class Test_ddnsRemove():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeOut = 2
        self.exp = {"code":0 , "msg": "Success", "action": "ddnsRemove"}
        self.ddnsRemoveClt = ddnsRemoveClient()
        self.idx = 0

    @pytest.mark.success
    def test_ddnsRemove_RES_1(self):
        time.sleep(self.timeOut)
        pload = self.ddnsRemoveClt.Create_ddnsRemove_Pload(index=self.idx)
        resBody = self.ddnsRemoveClt.ddnsRemove(self.cookie, pload=pload).body
        self.ddnsRemoveClt.assert_response(resBody,
                                        self.exp['code'],
                                        self.exp['msg'])

