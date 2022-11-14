import time

import serial
import serial.tools.list_ports
# ser = serial.Serial()

ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
  print("Port{} : desc {}: hwid {}".format(port, desc, hwid))
try:
  ser = serial.Serial( # set parameters, in fact use your own :-)
    port="COM24",
    baudrate=115200,
    bytesize=serial.SEVENBITS,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE
  )
except IOError: # if port is already opened, close it and open it again and print message
  print("Port in Use")
  pass

# ser.close()
