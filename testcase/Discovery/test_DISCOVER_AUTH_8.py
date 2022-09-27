import time

import pytest
from APIObject.discovery import discoveryClient
import Config.config as cfg
from Utilities import Utility as utl

class Test_Discovery():
    @pytest.fixture(autouse=True, scope="function")
    def set_up(self):
        self.disClt = discoveryClient()
        self.exp = {"code": 13, "msg": "Discovery Failed"}

    @pytest.mark.success
    def test_DISCOVER_AUTH_1(self):
        clientMAC1 = cfg.CLIENT_MAC
        md5 = utl.md5_encrypt(cfg.STR_ENCRYPT + clientMAC1, cfg.SALT)
        pload = self.disClt.Create_Discovery_Pload(authen=md5[:-1])
        resBody = self.disClt.discovery(pload=pload)
        self.disClt.assert_response(resBody,
                                    self.exp['code'],
                                    self.exp['msg'])
