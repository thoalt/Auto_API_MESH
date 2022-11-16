import time

import serial
import io


import Config.config as cfg

class Serial_Lib:
    def __init__(self, port=None, bitRate=None):
        if port is None:
            self.port = cfg.PORT_SER
        else:
            self.port = port

        if bitRate is None:
            self.bitRate = cfg.SPEED_RATE
        else:
            self.bitRate = bitRate

        self.con = serial.Serial(
            port=self.port,
            baudrate=self.bitRate,
            bytesize=8,
            timeout=5,
            stopbits=serial.STOPBITS_ONE
        )

    def Run_Command(self, command):
        self.con.flushInput()
        self.con.flushOutput()
        self.con.write(f"{command}\n".encode('utf8'))
        time.sleep(0.1)


    def Get_Ouput_From_Command(self, command, numLine=5):
        self.Login_To_Serial()
        self.Run_Command(command=command)
        # print("Run Command Success")
        output = self.con.readlines()[0:int(numLine)]
        # print("Get Output OK")
        # print(output)
        self.Close_Serial_Connect()
        return output

    def Login_To_Serial(self):
        self.con.close()
        self.con.open()
        self.Run_Command("\n")
        self.Run_Command(cfg.USER_SSH)
        self.Run_Command(cfg.PASS_SSH)
        # print("Login Serial Success")

    def Close_Serial_Connect(self):
        self.con.close()

    def Get_Mode_Mesh(self):
        meshModeLine = ""
        meshMode = ""
        cmd = "cat /etc/config/mode_mesh"
        output = self.Get_Ouput_From_Command(cmd, 5)
        for idx, line in enumerate(output):
            if cmd in line.decode('utf8'):
                meshModeLine = output[idx + 1].decode('utf8')
                break
        if "root" in meshModeLine:
            meshMode = meshModeLine.split("root")[0]
        # print("********* MESH MODE ***********")
        # print(meshMode)
        return meshMode

    def Get_Pass_GUI(self):
        passGUILine = ""
        passGUI = ""
        cmd = "cat /etc/config/lighttpd.user"
        output = self.Get_Ouput_From_Command(cmd, 5)

        for idx, line in enumerate(output):
            #print(line.decode('utf8'))
            if cmd in line.decode('utf8'):
                passGUILine = output[idx + 1].decode('utf8')
                #print(passGUILine)
                break
        if "root" in passGUILine:
            passGUI = passGUILine.split("root")[1][1:]
        # print("********* passGUI ***********")
        # print(passGUI)
        return passGUI

    def Get_SSID_Name(self, interface):
        ssidName = ''
        ssidNameLine = ''
        cmd = f'iwconfig {interface} | grep ESSID'
        output = self.Get_Ouput_From_Command(cmd, 5)

        for idx, line in enumerate(output):
            if "ESSID:" in line.decode('utf8'):
                ssidNameLine = output[idx].decode('utf8')
                break
        ssidName = ssidNameLine.split("ESSID:")[1].split('"')[1]
        # print("********* ssidName ***********")
        # print(ssidName)
        return ssidName

    def Get_IP_Address(self):
        ipAddLine = ""
        ipAddr = ""
        cmd = "ifconfig br-lan | grep 'inet addr'"
        output = self.Get_Ouput_From_Command(cmd, 5)
        #print(output)
        for idx, line in enumerate(output):
            if "inet addr:" in line.decode('utf8'):
                ipAddLine = line.decode('utf8')
                break

        ipAddr = ipAddLine.strip().split(" ")[1].split(":")[1]
        return ipAddr

    def Reset_Factory(self):
        self.Login_To_Serial()
        self.Run_Command("firstboot -y; reboot\n")
        time.sleep(240)
# print(f"{str(idx)}: {line.decode('utf8')}")
# classLib = Serial_Lib()
# classLib.Get_Pass_GUI()

