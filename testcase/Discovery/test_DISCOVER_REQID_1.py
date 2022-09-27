import time
import pytest
from APIObject.discovery import discoveryClient


class Test_Discovery():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.timeout = 2
        self.disClt = discoveryClient()
        self.exp = {"code": 0, "msg": "Success", "action": "discovery"}
        self.data = [0, 1, 2147483646, 2147483647]

    @pytest.mark.success
    def test_DISCOVER_ACT_1(self):
        resBody_Lst = []
        for item in self.data:
            pload = self.disClt.Create_Discovery_Pload(reqID=item)
            resBody = self.disClt.discovery(pload=pload)
            resBody_Lst.append(resBody)
            time.sleep(self.timeout)

        self.disClt.assert_response_list(resBody_Lst,
                                    self.exp['code'],
                                    self.exp['msg'],
                                    self.exp['action'])
