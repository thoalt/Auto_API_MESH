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
        # print("***************** RESPONSE BEFORE LOAD **********")
        # print(resBody)

        resBody = json.loads(resBody)
        print("***************** RESPONSE **********")
        print(json.dumps(resBody, indent=4))

        return Response(status_code, resBody, resHeaders)

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
    #     bodyStr = json.loads(bodyStr)
    #     return bodyStr