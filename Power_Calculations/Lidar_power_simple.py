import matplotlib.pyplot as plt
import numpy as np

PTX = 1.00    # Watts
GTX = 1       # Transmiter efficiency
GRX = 1       # Reciever efficiency
R = 1.0      # reciever radius in meters
Lmax = 10000        # distance from lidar to reflector

# Detector characteristics
Xilambda = 0.3    #A/Watt


#Range of L values
N=2000          # Number of range points
start=1
stop=Lmax
dx=(stop-start)/N

x=np.linspace(start, stop,N)
PRX=np.zeros(N)
Signal=np.zeros(N)
beta=np.zeros(N)



for i in range(N):
    PRX[i]=GTX*GRX*PTX*np.pi*R**2/(2*np.pi*x[i]**2)
    Signal[i]=PRX[i]*Xilambda
    beta[i]=10*np.log(Signal[i])

plt.figure()
plt.xlabel("Range[m]")
plt.ylabel("Signal current [mA]")
plt.plot(x, np.log(Signal))
plt.plot(x, beta)
#plt.plot(x,y_axis)
plt.show()
