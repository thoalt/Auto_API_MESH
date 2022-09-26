from assertpy import assert_that, soft_assertions
from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib

class TracerouteClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.url = cfg.url_Agent
        self.request = API_lib()

    def Create_TraceRoute_Pload(self, action=None, tracerouteCode=None, host=None, reqID=None):
        pload = cfg.req_traceroute

        payload = self.set_payload_with_action_reqID(pload=pload, action=action, reqID=reqID)

        if tracerouteCode is not None:
            payload['tracerouteCode'] = tracerouteCode
        else:
            payload['tracerouteCode'] = pload['tracerouteCode']

        if reqID is None:
            reqID = utl.random_requestID()
        payload['requestId'] = reqID

        if host is not None:
            payload['host'] = host
        else:
            payload['host'] = pload['host']
        return payload

    def traceroute(self, cookies=None, pload=None):
        if pload is None:
            payload = self.Create_TraceRoute_Pload()
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, cookies=cookies, pload=payload)
        return response

    def assert_trace(self, resBody, status, msg, action=None, traceCode=None, host=None, hostAddr=None, hopCnt=None):
        with soft_assertions():
            assert_that(resBody['status']).is_equal_to(status)
            assert_that(resBody['message']).is_equal_to(msg)

            if action is not None:
                actionRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..action")
                assert_that(actionRes).is_equal_to(action)

            if traceCode is not None:
                traceRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..tracerouteCode")
                assert_that(traceRes).is_equal_to(traceCode)

            if host is not None:
                hostRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..host")
                assert_that(hostRes).is_equal_to(host)

            if hostAddr is not None:
                hostAddrRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..hostAddress")
                assert_that(hostAddrRes).is_equal_to(hostAddr)

            if hopCnt is not None:
                hopRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..hopCount")
                assert_that(hopRes).is_equal_to(hopCnt)

    def assert_trace_lst(self, resBodyLst, status, msg, action=None, traceCode=None, host=None, hostAddr=None, hopCnt=None):
        with soft_assertions():
            for resBody in resBodyLst:
                self.assert_trace(resBody, status, msg, action=action,
                                  traceCode=traceCode, host=host, hostAddr=hostAddr, hopCnt=hopCnt)

    def get_result(self, resBody):
        resultRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..results")
        return resultRes[0]


