import time
from assertpy import assert_that
from sshaolin.client import SSHClient
from APIObject.openssesion import openssesionClient
from APIObject.login import LoginClient
from APIObject.logout import LogoutClient
from Utilities import Utility as utl
from Config import config as cfg

# # SSH to Mesh AP and restart vnptt_mad agent
# client = SSHClient(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH)
# SSHShell = client.create_shell()
# SSHShell.execute_command('/etc/init.d/vnptt_mad stop')
# time.sleep(1)
# SSHShell.execute_command('/etc/init.d/vnptt_mad start')
# time.sleep(1)
# SSHShell.close()

# Open session then Login
ClientSes = openssesionClient()
cookie = ClientSes.Open_Sesion_And_Get_Cookie()

# Login
LoginClt = LoginClient()
LoginClt.login(cookie)

print("************ COOKIE ********************")
print(cookie)