import copy
from assertpy import soft_assertions, assert_that
from cerberus import Validator
from Utilities import Utility as utl
from Config import Schema_Template as scTmp


class BaseClient:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        self.headersCurl = ["Content-Type: application/json", "Accept:application/json"]

    def get_response_data(self, resBody):
        dataDic = resBody["data"]
        return dataDic

    def set_payload_with_action_reqID(self, pload, action=None, reqID=None):
        pload_new = copy.deepcopy(pload)

        if action is not None:
            pload_new['action'] = action
        else:
            pload_new['action'] = pload['action']

        if reqID is None:
            reqID = utl.random_requestID()
        pload_new['requestId'] = reqID

        return pload_new

    def assert_val(self, expecVal, actualVal, desc=''):
        with soft_assertions():
            assert_that(expecVal, description=desc).is_equal_to(actualVal)

    def assert_val_lst(self, expecVal_Lst, actualVal_Lst):
        with soft_assertions():
            for idx, item in enumerate(expecVal_Lst):
                assert_that(str(expecVal_Lst[idx]), description=str(item)).is_equal_to(str(actualVal_Lst[idx]))

    def assert_response(self, resBody, status, msg, action=None):
        with soft_assertions():
            assert_that(resBody['status'], description="STATUS ERROR").is_equal_to(status)
            assert_that(resBody['message'], description="MESSAGE ERROR").is_equal_to(msg)

            if action is not None:
                actionRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..action")
                assert_that(actionRes, description="ACTION ERROR").is_equal_to(action)

    def assert_response_list(self, resBody_lst, status, msg, action=None):
        with soft_assertions():
            for resBody in resBody_lst:
                self.assert_response(resBody=resBody,
                                    status=status,
                                    msg=msg,
                                    action=action)

    def get_result(self, resBody):
        resultRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..results")
        return resultRes

    def valid_schema_common(self, resBody, schema=None, require_all=True):

        if schema is None:
            schema = scTmp.schema_common

        valid = Validator(schema=schema, require_all=require_all)
        is_valid = valid.validate(resBody)
        assert_that(is_valid, description=valid.errors).is_true()

    def valid_schema_topo_common(self, resBody, schema=scTmp.schema_topo_common, require_all=True):
        valid = Validator(schema=schema, require_all=require_all)
        is_valid = valid.validate(resBody)
        assert_that(is_valid, description=valid.errors).is_true()

    def valid_schema_resul(self, resBody, schema, require_all=True):
        resultRes = utl.search_nodes_using_json_path(resBody, jsonPath="$..results")
        for item in resultRes:
            valid = Validator(schema=schema, require_all=require_all)
            is_valid = valid.validate(item)
            assert_that(is_valid, description=valid.errors).is_true()

    def valid_schema_client(self, resBody, schema, require_all=True):
        clientInfo = utl.search_nodes_using_json_path(resBody, jsonPath="$..results[*].clientInfo")
        for client in clientInfo:
            valid = Validator(schema=schema, require_all=require_all)
            is_valid = valid.validate(client)
            assert_that(is_valid, description=valid.errors).is_true()

    def Remove_Key_In_Pload(self, dictBefore, key):
        dictCopy = copy.deepcopy(dict(dictBefore))
        del dictCopy[key]
        return dictCopy

    def Remove_Attribute_In_Pload(self, dictBefore: dict):
        pload_list = []
        keyLst = dictBefore.keys()
        for key in keyLst:
            if key != 'requestId':
                newDict = self.Remove_Key_In_Pload(dictBefore, key)
                pload_list.append(newDict)
        return pload_list

    def Remove_Attribute_Without_Action_RequestID(self, dictBefore: dict):
        pload_list = []
        keyLst = dictBefore.keys()
        for key in keyLst:
            if key not in ['requestId', 'action']:
                newDict = self.Remove_Key_In_Pload(dictBefore, key)
                pload_list.append(newDict)
        return pload_list

    def Remove_Request_ID_In_Pload(self, dictBefore: dict):
        pload_list = []
        keyLst = dictBefore.keys()
        for key in keyLst:
            if key == 'requestId':
                newDict = self.Remove_Key_In_Pload(dictBefore, key)
                pload_list.append(newDict)
                break
        return pload_list

