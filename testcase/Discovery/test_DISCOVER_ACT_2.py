import time

import pytest
from APIObject.discovery import discoveryClient


class Test_Discovery():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.disClt = discoveryClient()
        self.exp = {"code": 8, "msg": "Invalid Action"}
        self.data = ['discovery1','discover']

    @pytest.mark.success
    def test_DISCOVER_ACT_1(self):
        resBody_Lst = []
        for item in self.data:
            pload = self.disClt.Create_Discovery_Pload(action=item)
            resBody = self.disClt.discovery(pload=pload)
            resBody_Lst.append(resBody)
            time.sleep(3)
        self.disClt.assert_response_list(resBody_Lst,
                                    self.exp['code'],
                                    self.exp['msg'])
