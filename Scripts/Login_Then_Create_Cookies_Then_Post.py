import copy
import json
import time
from dataclasses import dataclass
from io import BytesIO
import random
import pycurl
from passlib import hash
import requests

IP_ADDR_CAP = "192.168.88.1"
CLIENT_MAC = "00:0E:C6:59:A1:A6"
SALT = "D2...40."
STR_ENCRYPT = "VNPT"
SERIAL = "1292922130B4454"
headersCurl = ["Content-Type: application/json", "Accept:application/json"]

FW_Name = "EW12_EW12ST000T0004.tar.gz"
FW_Path = "E:\Auto_WorkingTesting\Auto_API_MESH\Drivers\\" + FW_Name

url_Login = f"https://{IP_ADDR_CAP}:9000/onelinklogin"
url_Agent = f"https://{IP_ADDR_CAP}:9000/onelinkagent"
url_Upload = f"https://{IP_ADDR_CAP}:9000/onelinkagent/files/{FW_Name}"
url_Broadcast = f"https://255.255.255.255:9000"

req_openSession = {
    "action": "openSession",
    "clientMac": "<clientMac>",
    "authenString": "<authenString>",
    "requestId": "<requestId>"
}


@dataclass
class Response:
    status_code: int
    body: str
    headers: str


def md5_encrypt(password, salt):
    """
    Description: Using md5 encryption to generator Password hash
    """
    return hash.md5_crypt.hash(password, salt=salt)


def random_requestID():
    """
    Description:
    """
    return random.randint(1, 20000)


def post(url, headers=None, verify=False, cookies=None, pload=None):
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
    # print("***************** HEADER **********")
    # print(resHeaders)
    resBody = rawBody.getvalue().decode('UTF-8')
    # print("***************** RESPONSE BEFORE LOAD **********")
    # print(resBody)

    resBody = json.loads(resBody)
    print("***************** RESPONSE **********")
    print(json.dumps(resBody, indent=4))

    return Response(status_code, resBody, resHeaders)


def uploadFile(url, headers=None, verify=False, cookies=None, filePath=None):
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.HTTPHEADER, headers)
    if not verify:
        c.setopt(c.SSL_VERIFYPEER, 0)
    else:
        c.setopt(c.SSL_VERIFYPEER, 1)

    c.setopt(c.HTTPPOST, [("parameters", (c.FORM_FILE, filePath))])

    if cookies is not None:
        c.setopt(c.COOKIE, cookies)
    try:
        c.perform()
    except Exception as ex:
        print(str(ex))
    c.close()


def Create_OpenSession_Pload(action=None, clientMac=None, authen=None, reqID=None):
    ploadOrg = req_openSession
    pload = copy.deepcopy(ploadOrg)

    if action is not None:
        pload['action'] = action
    else:
        pload['action'] = ploadOrg['action']

    if clientMac is not None:
        pload['clientMac'] = clientMac
    else:
        pload['clientMac'] = CLIENT_MAC

    if authen is not None:
        pload['authenString'] = authen
    else:
        pload['authenString'] = md5_encrypt(STR_ENCRYPT + pload['clientMac'], SALT)

    if reqID is None:
        pload['requestId'] = random.randint(1, 20000)
    else:
        pload['requestId'] = reqID

    return pload


def Get_SessionID(resHeaders):
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
                    salt = val.split("=")[1]
    return sesID, salt


def Create_Cookie(sessionID=None, md5=None):
    """
         Description: create cookies from session ID and salt which get from Open Session
        """
    cookie = f"SESSIONID={sessionID};md5={md5}"

    print("***************** COOKIE **************")
    print(cookie)
    return cookie


def Calculate_md5(sessionID=None, conStr=None, salt=None, serial=None, authen=None):
    if serial is None:
        serial = SERIAL

    if conStr is None:
        conStr = "On3L1nk"
    authenStr = sessionID + conStr + serial

    # print("************* AUTHEN *************")
    # print(authenStr)
    md5 = md5_encrypt(authenStr, salt)
    return md5


def Open_Session_And_Get_Session_ID(reqID=None):
    """
        Description: Open new session to get header, then return the session ID, salt and request ID
        """

    payload = Create_OpenSession_Pload(reqID)
    response = post(url=url_Login, headers=headersCurl, pload=payload)

    sesID, salt = Get_SessionID(response.headers)
    return sesID, salt, reqID


def Open_Sesion_And_Get_Cookie():
    sesID, salt, reqID = Open_Session_And_Get_Session_ID()
    md5Cal = Calculate_md5(sessionID=sesID, salt=salt, serial=SERIAL)
    cookie = Create_Cookie(sessionID=sesID, md5=md5Cal)
    return cookie


def login(cookies):
    response = post(url=url_Login, headers=headersCurl, cookies=cookies)
    return response


if __name__ == '__main__':
    print("************* Open Session and get Cookie *************")
    cookie = Open_Sesion_And_Get_Cookie()
    print("************* LOGIN *************")
    response = login(cookies=cookie)

    print("************* Upload File *************")
    reqHeaders = {"Cookie": cookie}
    print("FW_PATH = " + FW_Path)

    # resFW = uploadFile(url=url_Upload,
    #                    headers=headersCurl,
    #                    cookies=cookie,
    #                    filePath=FW_Path)

    # try:
    #     with open(FW_Path, 'rb') as fobj:
    #         print("URL_UPLOAD = " + url_Upload)
    #         print("HEADER = " + str(reqHeaders))
    #         print("DATA = " + str(fobj))
    #         resFW = requests.post(url_Upload, headers={"Cookie": cookie},  data=fobj, verify=False)
    #
    # except Exception as ex:
    #     print(str(ex))

    print("************* Other API *************")
    # req_CreateMesh = {
    #     "action": "meshCreate",
    #     "requestId": 18581,
    #     "meshMode": 2,
    #     "ssidName": "ThoaTest_1659",
    #     "password": "1234567890_90",
    #     "addNode": False,
    #     "repeaterSsidName": "1111_AP_Wireless_Test_2GHz",
    #     "repeaterAuthenMode": "OPEN"
    # }
    # resPonse = post(url=url_Agent, headers=headersCurl, cookies=cookie, pload=req_CreateMesh)
    # # resBody = resPonse.body
    # time.sleep(180)
    #
    # req_MeshView = {
    #     "action": "meshView",
    #     "requestId": 8098
    # }
    # resPonse2 = post(url=url_Agent, headers=headersCurl, cookies=cookie, pload=req_MeshView)
    #
    # time.sleep(3)
    #
    # req_SSIDView = {
    #     "action": "ssid5GView",
    #     "requestId": 7463
    # }
    # resPonse3 = post(url=url_Agent, headers=headersCurl, cookies=cookie, pload=req_SSIDView)

    request = {
    "action": "meshCreate",
    "requestId": 8038,
    "meshMode": 0,
    "ssidName": "`",
    "password": "1234567890_160",
    "addNode": False
}
    resPonse4 = post(url=url_Agent, headers=headersCurl, cookies=cookie, pload=request)