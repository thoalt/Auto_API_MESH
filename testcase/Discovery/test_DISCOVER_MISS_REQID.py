import json
import time

import pytest
from APIObject.discovery import discoveryClient


class Test_Discovery():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.disClt = discoveryClient()
        self.exp = {"code": 9, "msg": "Miss Request ID"}
        pload = self.disClt.Create_Discovery_Pload()
        self.data = [self.disClt.Remove_Key_In_Pload(pload, 'requestId')]


    def test_DISCOVER_ACT_1(self):
        resBody_Lst = []
        for item in self.data:
            print(json.dumps(item, indent=4))
            time.sleep(2)
            resBody = self.disClt.discovery(pload=item)
            resBody_Lst.append(resBody)
            time.sleep(3)
        self.disClt.assert_response_list(resBody_Lst,
                                    self.exp['code'],
                                    self.exp['msg'])
