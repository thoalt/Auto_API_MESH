from assertpy import assert_that, soft_assertions
from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib

class PingClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_Ping_Pload(self, action=None, pingCode=None, host=None, reqID=None):
        pload = cfg.req_ping

        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if pingCode is not None:
            payload['pingCode'] = pingCode
        else:
            payload['pingCode'] = pload['pingCode']

        if reqID is None:
            reqID = utl.random_requestID()
        payload['requestId'] = reqID

        if host is not None:
            payload['host'] = host
        else:
            payload['host'] = pload['host']
        return payload

    def ping(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_Ping_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def assert_ping(self, resBody, status, msg, action=None):
        with soft_assertions():
            assert_that(resBody['status']).is_equal_to(status)
            assert_that(resBody['message']).is_equal_to(msg)

            if action is not None:
                actionRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..action")
                assert_that(actionRes).is_equal_to(action)

    def assert_ping_lst(self, resBodyLst, status, msg, action=None, pingCode=None):
        with soft_assertions():
            for resBody in resBodyLst:
                assert_that(resBody['status']).is_equal_to(status)
                assert_that(resBody['message']).is_equal_to(msg)

                if action is not None:
                    actionRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..action")
                    assert_that(actionRes).is_equal_to(action)

                if pingCode is not None:
                    resultRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..results")[0]
                    assert_that(resultRes['pingCode']).is_equal_to(pingCode)

    def get_result(self, resBody):
        resultRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..results")
        return resultRes[0]

    def assert_result(self, resultRes, pingCode=None, host=None, cntPass=None, cntFail=None):
        with soft_assertions():
            if pingCode is not None:

                assert_that(resultRes['pingCode']).is_equal_to(pingCode)

            if host is not None:
                assert_that(resultRes['host']).is_equal_to(host)

            if cntPass is not None:
                assert_that(resultRes['successCount']).is_equal_to(cntPass)

            if cntFail is not None:
                assert_that(resultRes['failureCount']).is_equal_to(cntFail)


