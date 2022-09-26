IP_ADDR_CAP = "192.168.88.1"
CLIENT_MAC = "D8:D0:90:3A:94:D6"
SALT = "D2...40."
STR_ENCRYPT = "VNPT"
SERIAL = "1290912164A242A"

SSID = "API_TEST_ThoaLT"
PASSWORD = "1234567890"
auth = "WPA2PSK"
encrypt = "AES"
GUID = "{829d9c08-9781-498b-8677-4cecbddc1c1d}"

BSSIDList_MeshOnly = [
    "A4:F4:C2:0B:44:55",
    "A4:F4:C2:0B:44:56",
    "A4:F4:C2:0B:44:69",
    "A4:F4:C2:0B:44:6A"
]

BSSIDList_MeshONT = [
    "A4:F4:C2:0B:44:55",
    "A4:F4:C2:0B:44:56",
    "A4:F4:C2:0B:44:69",
    "A4:F4:C2:0B:44:6A"
]

MIN_TIMEOUT = 2
MAX_TIMEOUT = 30
AVG_TIMEOUT = 10

USER_SSH = "root"
PASS_SSH = "VNPT@88Tech"
PORT_NUM = "22"

url_Login = f"https://{IP_ADDR_CAP}:9000/onelinklogin"
url_Agent = f"https://{IP_ADDR_CAP}:9000/onelinkagent"
url_Broadcast = f"https://255.255.255.255:9000"

# GUI INFORMATION
CAP_URL = f"http://{IP_ADDR_CAP}/"
USER_GUI = "root"
PASS_GUI = "VNPT"

req_discovery = {
    "action": "discovery",
    "clientMac": "<clientMac>",
    "authenString": "<authenString>",
    "requestId": "<requestId>"
}

req_openSession = {
    "action": "openSession",
    "clientMac": "<clientMac>",
    "authenString": "<authenString>",
    "requestId": "<requestId>"
}

req_logout = {
    "action": "logout",
    "requestId": "<requestId>"
}

req_reboot = {
    "action": "reboot",
    "macList": "<macList>",
    "requestId": "<requestId>"
}

req_reset = {
    "action": "reset",
    "macList": "<macList>",
    "requestId": "<requestId>"
}

req_lanview = {
    "action": "lanView",
    "requestId": "<requestId>"
}

req_wanViewConfig = {
    "action": "wanViewConfig",
    "requestId": "<requestId>"
}

req_radio2GView = {
    "action": "radio2.4GView",
    "requestId": "<requestId>"
}

req_radio5GView = {
    "action": "radio5GView",
    "requestId": "<requestId>"
}

req_deviceInfoView = {
    "action": "deviceInfoView",
    "requestId": "<requestId>"
}

req_networkinfoView = {
    "action": "networkinfoView",
    "requestId": "<requestId>"
}

req_passwordEdit = {
    "action": "passwordEdit",
    "username": "<username>",
    "password": "<password>",
    "requestId": "<requestId>"
}

req_speedtest = {
    "action": "speedtest",
    "requestId": "<requestId>"
}

req_ping = {
    "action": "ping",
    "pingCode": 1,
    "host": "<host domain name or IP address>",
    "requestId": "<requestId>"
}

req_traceroute = {
    "action": "traceroute",
    "tracerouteCode": 1,
    "host": "<host domain name or IP address>",
    "requestId": "<requestId>"
}

req_topology = {
    "action": "topology",
    "requestId": "<requestId>"
}


req_addNewNode = {
    "action": "addNewNode",
    "requestId": "<requestId>"
}


req_syncONTConfig = {
    "action": "syncONTConfig",
    "requestId": "<requestId>",
    "enableSync": False
}
