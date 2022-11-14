import math
#
# # bw = 20
# fm=4*10**3     #Bandwidth of PCM
# xmax=3.8
# snr=100       #Signal to Noise Ratio
# outputs=30.0
# v=7.0

#Calculation
# bw=outputs*v*fm
bwInMhz = 20
bwInHz = bwInMhz * 1000000

rate = 2 * bwInHz * math.log2(4)
m = math.pow(2, 86.7/80)
print(m)
QAM = 256
BW = 20
BR = BW * (math.log2(QAM))

print(BR)