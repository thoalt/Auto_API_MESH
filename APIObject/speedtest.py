from assertpy import assert_that, soft_assertions
from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib

class SpeedTestClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_SpeedTest_Pload(self, action=None, reqID=None):
        pload = cfg.req_speedtest
        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)
        return payload

    def speedtest(self, cookies=None, pload=None ):
        if pload is None:
            payload = self.Create_SpeedTest_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def assert_speedtest(self, resBody, status, msg, action=None, speedCode=None):
        with soft_assertions():
            assert_that(resBody['status']).is_equal_to(status)
            assert_that(resBody['message']).is_equal_to(msg)

            if action is not None:
                actionRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..action")
                assert_that(actionRes).is_equal_to(action)

            if speedCode is not None:
                resultRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..results")[0]
                assert_that(resultRes['speedtestCode']).is_equal_to(speedCode)

    def assert_speedtest_lst(self, resBody_lst, status, msg, action=None, speedCode=None):
        with soft_assertions():
            for resBody in resBody_lst:
                self.assert_speedtest(resBody=resBody,
                                      status=status,
                                      msg=msg,
                                      action=action,
                                      speedCode=speedCode)