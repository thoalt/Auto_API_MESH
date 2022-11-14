import pytest
from APIObject.discovery import discoveryClient
from Config import Schema_Template as scTmp

class Test_Discovery():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.disClt = discoveryClient()


    def test_DISCOVER_SCHEMA_1(self):
        resBody = self.disClt.discovery()
        self.disClt.valid_schema_common(resBody)
        self.disClt.valid_schema_resul(resBody, schema=scTmp.schema_discovery_result)