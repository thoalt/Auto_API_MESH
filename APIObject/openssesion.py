import copy
from assertpy import assert_that, soft_assertions, soft_fail
from APIObject.baseClient import BaseClient
from Config import config as cfg
from Utilities import Utility as utl
from base.APILib import API_lib


class openssesionClient(BaseClient):
    def __init__(self, url=None):
        super().__init__()
        if url != None:
            self.url = url
        else:
            self.url = cfg.url_Login
        self.request = API_lib()


    def Create_OpenSession_Pload(self, action=None, clientMac=None, authen=None, reqID=None):
        ploadOrg = cfg.req_openSession
        pload = copy.deepcopy(ploadOrg)

        if action is not None:
            pload['action'] = action
        else:
            pload['action'] = ploadOrg['action']

        if clientMac is not None:
            pload['clientMac'] = clientMac
        else:
            pload['clientMac'] = cfg.CLIENT_MAC

        if authen is not None:
            pload['authenString'] = authen
        else:
            pload['authenString'] = utl.md5_encrypt(cfg.STR_ENCRYPT + pload['clientMac'], cfg.SALT)

        if reqID is None:
            pload['requestId'] = utl.random_requestID()
        elif reqID == "Empty":
            pload['requestId'] = None
        else:
            pload['requestId'] = reqID

        return pload

    def Open_Session(self, reqID=None, pload=None):
        """
        Description: Open new session then return the response message
        """
        if pload is None:
            payload = self.Create_OpenSession_Pload(reqID=reqID)
        else:
            payload = pload

        response = self.request.post(url=self.url, headers=self.headersCurl, pload=payload)
        return payload['requestId'], response

    def Get_SessionID(self, resHeaders):
        """
        Get Session ID and Salt from response headers when open new session
        """
        sesID, salt = '', ''
        lines = resHeaders.splitlines()
        for line in lines:
            if "SESSIONID" in line:
                lstVal = line.split(":")[1].split(";")
                for val in lstVal:
                    if "SESSIONID" in val:
                        sesID = val.split("=")[1]
                    if "salt" in val:
                        salt = val.split("=")[1][0:8]
        # print("**** SESIONID: ***" + str(sesID))
        # print("**** SALT: ***" + str(salt))

        return sesID, salt

    def Open_Session_And_Get_Session_ID(self, reqID=None):
        """
        Description: Open new session to get header, then return the session ID, salt and request ID
        """

        payload = self.Create_OpenSession_Pload(reqID)
        # print(self.url)
        response = self.request.post(url=self.url, headers=self.headersCurl, pload=payload)

        sesID, salt = self.Get_SessionID(response.headers)
        return sesID, salt, reqID

    def Gen_Authen(self, sessionID=None, conStr=None, serial=None):
        if serial is None:
            serial = cfg.SERIAL

        if conStr is None:
            conStr = "On3L1nk"

        authenStr = sessionID + conStr + serial
        return authenStr

    def Calculate_md5(self, sessionID=None, conStr=None, salt=None, serial=None, authen=None):
        if serial is None:
            serial = cfg.SERIAL

        if conStr is None:
            conStr = "On3L1nk"

        if authen is None:
            authenStr = self.Gen_Authen(sessionID, conStr, serial)
        else:
            authenStr = authen

        # print("************* AUTHEN *************")
        # print(authenStr)
        md5 = utl.md5_encrypt(authenStr, salt)
        return md5

    def Create_Cookie(self, sessionID=None, md5=None):
        """
         Description: create cookies from session ID and salt which get from Open Session
        """

        cookie = f"SESSIONID={sessionID};md5={md5}"

        print("***************** COOKIE **************")
        print(cookie)

        return cookie

    def Open_Sesion_And_Get_Cookie(self):
        sesID, salt, reqID = self.Open_Session_And_Get_Session_ID()
        md5Cal = self.Calculate_md5(sessionID=sesID, salt=salt, serial=cfg.SERIAL)
        cookie = self.Create_Cookie(sessionID=sesID, md5=md5Cal)

        return cookie

    def assert_opensession(self, resBody, status, msg, reqID=None, action=None):
        with soft_assertions():
            assert_that(resBody['status']).is_equal_to(status)
            assert_that(resBody['message']).is_equal_to(msg)
            if reqID is not None:
                assert_that(resBody['requestId']).is_equal_to(reqID)

    def assert_opensession_List(self, resBodyLst, status, msg, reqID=None, action=None):
        with soft_assertions():
            for resBody in resBodyLst:
                assert_that(resBody['status']).is_equal_to(status)
                assert_that(resBody['message']).is_equal_to(msg)
                if reqID is not None:
                    assert_that(resBody['requestId']).is_equal_to(reqID)

    def assert_same_sesionID(self, sesID1, sesID2):
        assert_that(sesID2, description=["SESSIONID"]).is_equal_to(sesID1)

    def assert_def_sesionID(self, sesID1, sesID2):
        assert_that(sesID2, description=["SESSIONID"]).is_not_equal_to(sesID1)