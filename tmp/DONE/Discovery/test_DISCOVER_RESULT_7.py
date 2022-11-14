import pytest
from APIObject.discovery import discoveryClient


class Test_Discovery():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.disClt = discoveryClient()
        self.exp = {"code": 0, "msg": "Success", "action": "discovery"}

    @pytest.mark.skip(reason="This is Manual Testcase")
    def test_DISCOVER_ACT_1(self):
        resBody = self.disClt.discovery()
        self.disClt.assert_response(resBody,
                                    self.exp['code'],
                                    self.exp['msg'],
                                    self.exp['action'])
