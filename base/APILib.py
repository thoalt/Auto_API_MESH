import pycurl
import json
from io import BytesIO
from Config import config as cfg
from Utilities import Utility as utl
from dataclasses import dataclass


@dataclass
class Response:
    status_code: int
    body: str
    headers: str


class API_lib:
    def post(self, url, headers=None, verify=False, cookies=None, pload=None):
        rawHeaders = BytesIO()
        rawBody = BytesIO()

        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.HTTPHEADER, headers)
        if not verify:
            c.setopt(c.SSL_VERIFYPEER, 0)
        else:
            c.setopt(c.SSL_VERIFYPEER, 1)

        c.setopt(c.POST, 1)

        if cookies is not None:
            c.setopt(c.COOKIE, cookies)

        if pload is not None:
            print("\n***************** PAYLOAD **********")
            print(json.dumps(pload, indent=4))
            c.setopt(c.POSTFIELDS, json.dumps(pload))

        c.setopt(c.HEADERFUNCTION, rawHeaders.write)
        c.setopt(c.WRITEFUNCTION, rawBody.write)
        status_code = c.getinfo(pycurl.HTTP_CODE)

        try:
            c.perform()
        except:
            pass
        c.close()

        resHeaders = rawHeaders.getvalue().decode('UTF-8')
        print("***************** HEADER **********")
        print(resHeaders)
        resBody = rawBody.getvalue().decode('UTF-8')
        # print("***************** RESPONSE **********")
        # print(json.dumps(resBody, indent=4))

        resBody = json.loads(resBody)

        # try:
        #     resBody = json.loads(resBody)
        # except:
        #     #### TODO: Need to remove after
        #     resBody = self.get_body_from_header(resHeaders)
        print("***************** RESPONSE **********")
        print(json.dumps(resBody, indent=4))

        return Response(status_code, resBody, resHeaders)

    def get_body_from_header(self, resHeaders) -> dict:
        lines = resHeaders.splitlines()
        bodyStr = "{"
        for line in lines:
            if "status" in line:
                bodyStr = bodyStr + line

            if "message" in line:
                bodyStr = bodyStr + line

            if "requestId" in line:
                bodyStr = bodyStr + line

            if "data" in line:
                bodyStr = bodyStr + line + "}}"
        bodyStr = json.loads(bodyStr)
        return bodyStr

    # def run_curl_cmd(self, url, headers=None, verify=False, cookies=None, pload=None):
    #     rawHeaders = BytesIO()
    #     rawBody = BytesIO()
    #
    #     c = pycurl.Curl()
    #
    #     c.setopt(c.URL, url)
    #
    #     c.setopt(c.HTTPHEADER, headers)
    #
    #     if not verify:
    #         c.setopt(c.SSL_VERIFYPEER, 0)
    #     else:
    #         c.setopt(c.SSL_VERIFYPEER, 1)
    #
    #     c.setopt(c.POST, 1)
    #
    #     if cookies is not None:
    #         c.setopt(c.COOKIE, cookies)
    #
    #     if pload is not None:
    #         c.setopt(c.POSTFIELDS, json.dumps(pload))
    #
    #     c.setopt(c.HEADERFUNCTION, rawHeaders.write)
    #     c.setopt(c.WRITEFUNCTION, rawBody.write)
    #
    #
    #     try:
    #         c.perform()
    #     except:
    #         pass
    #     c.close()
    #     status_code = c.getinfo(pycurl.HTTP_CODE)
    #
    #     resHeaders = rawHeaders.getvalue().decode('UTF-8')
    #     resBody = rawBody.getvalue().decode('UTF-8')
    #
    #     print("Runcurl_Cmd HEADER: " + resHeaders)
    #     print("Runcurl_Cmd BODY: " + resBody)
    #
    #     return Response(status_code, resBody, resHeaders)
    #
    # def get_sessionID(self, resHeaders):
    #     """
    #     Get Session ID and Salt from response headers when open new session
    #     """
    #     sesID, salt = '', ''
    #     lines = resHeaders.splitlines()
    #     for line in lines:
    #         if "SESSIONID" in line:
    #             lstVal = line.split(":")[1].split(";")
    #             for val in lstVal:
    #                 if "SESSIONID" in val:
    #                     sesID = val.split("=")[1]
    #                 if "salt" in val:
    #                     salt = val.split("=")[1]
    #     return sesID, salt
    #
    # def Open_Session(self, reqID=None):
    #     """
    #     Description: Open new session then return the response message
    #     """
    #     dataRaw = cfg.req_openSession
    #     if reqID is None:
    #         reqID = utl.random_requestID()
    #     dataRaw['clientMac'] = cfg.CLIENT_MAC
    #     dataRaw['authenString'] = utl.md5_encrypt(cfg.STR_ENCRYPT + cfg.CLIENT_MAC, cfg.SALT)
    #     dataRaw['requestId'] = reqID
    #
    #     resHeader, resBody = self.run_curl_cmd(url=self.url_login, headers=self.headers, pload=dataRaw)
    #     resBody = json.loads(resBody)
    #
    #     return reqID, resBody
    #
    # def Open_Session_And_Get_Session_ID(self, reqID=None):
    #     """
    #     Description: Open new session to get header, then return the session ID, salt and request ID
    #     """
    #     dataRaw = cfg.req_openSession
    #     if reqID is None:
    #         reqID = utl.random_requestID()
    #     dataRaw['clientMac'] = cfg.CLIENT_MAC
    #     dataRaw['authenString'] = utl.md5_encrypt(cfg.STR_ENCRYPT + cfg.CLIENT_MAC, cfg.SALT)
    #     dataRaw['requestId'] = reqID
    #
    #     resHeader, resBody = self.run_curl_cmd(url=self.url_login, headers=self.headers, pload=dataRaw)
    #     sesID, salt = self.get_sessionID(resHeader)
    #     return sesID, salt, reqID
    #
    # def create_cookies(self, sessionID, salt, serial=cfg.SERIAL):
    #     """
    #      Description: create cookies from session ID and salt which get from Open Session
    #     """
    #     authenStr = sessionID + "On3L1nk" + serial
    #     md5 = utl.md5_encrypt(authenStr, salt)
    #
    #     cookie = f"SESSIONID={sessionID};md5={md5}"
    #
    #     print("COOKIE: " + cookie)
    #     return cookie
    #
    # def login(self, cookies):
    #     resHeader, resBody = self.run_curl_cmd(url=self.url_login, headers=self.headers, cookies=cookies)
    #     print("LOGIN  HEADER: " + resHeader)
    #     print("LOGIN BODY: " + resBody)
    #     if resBody is not None:
    #         resBody = json.loads(resBody)
    #     return [resHeader, resBody]
    #
    # def get_response_data(self, resBody):
    #     dataDic = resBody["data"]
    #     return dataDic
    #
    # def get_body_from_header(self, resHeaders) -> dict:
    #     lines = resHeaders.splitlines()
    #     bodyStr = "{"
    #     for line in lines:
    #         if "status" in line:
    #             bodyStr = bodyStr + line
    #
    #         if "message" in line:
    #             bodyStr = bodyStr + line
    #
    #         if "requestId" in line:
    #             bodyStr = bodyStr + line
    #
    #         if "data" in line:
    #             bodyStr = bodyStr + line + "}}"
    #     print("Body: " + bodyStr)
    #     bodyStr = json.loads(bodyStr)
    #     return bodyStr
    #
    # def view_24G_ssid(self, cookies, reqID=None):
    #     dataRaw = cfg.req_ssid24GView
    #     if reqID is None:
    #         reqID = utl.random_requestID()
    #     dataRaw['requestId'] = reqID
    #
    #     resHeader, resBody = self.run_curl_cmd(url=self.url_agent, headers=self.headers, cookies=cookies, pload=dataRaw)
    #
    #     if resBody is not None:
    #         resBody = json.loads(resBody)
    #     return resBody
    #
    # def view_info(self, cookies, pload, reqID=None):
    #     if reqID is None:
    #         reqID = utl.random_requestID()
    #     pload['requestId'] = reqID
    #
    #     resHeader, resBody = self.run_curl_cmd(url=self.url_agent, headers=self.headers, cookies=cookies, pload=pload)
    #
    #     if resBody is not None:
    #         resBody = json.loads(resBody)
    #     return resBody
    #
    # def edit_SILD(self, cookies, pload, action=None, slidName=None, reqID=None):
    #     if action is not None:
    #         pload['action'] = action
    #
    #     if reqID is None:
    #         reqID = utl.random_requestID()
    #     pload['requestId'] = reqID
    #
    #     if slidName is not None:
    #         pload['slid'] = slidName
    #
    #     print(pload)
    #
    #     resHeader, resBody = self.run_curl_cmd(url=self.url_agent, headers=self.headers, cookies=cookies, pload=pload)
    #
    #     print(resHeader)
    #     print(resBody)
    #
    #     if resBody is not None:
    #         resBody = json.loads(resBody)
    #     return resBody
