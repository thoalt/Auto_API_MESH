from base.WiFiLib import Wifi_lib
from base.SSHLib import SSH_Lib
from sshaolin.client import SSHClient, SSHShell
from Config import config as cfg

wifiClt = Wifi_lib()

wifiClt.connect_wifi(ssid="EW_21ce7a", passwd="EW@21ce7a", bssid="A4:F4:C2:21:CE:7C")
client = SSHClient(hostname=cfg.IP_ADDR_CAP, username=cfg.USER_SSH, password=cfg.PASS_SSH, timeout=300)
sshShelClt= client.create_shell()
sshShelClt.execute_command("uci set wsplcd.config.WriteDebugLogToFile=APPEND; uci commit wsplcd; /etc/init.d/wsplcd restart")

sshShelClt.close()
wifiClt.disconnect()