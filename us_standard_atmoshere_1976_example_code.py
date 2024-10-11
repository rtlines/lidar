import numpy as np
import matplotlib.pyplot as plt
import ussa1976

# Call the routine that calculates values for the US Standard Atmosphere (1976)
#   The values come back in a data structure. If the stucture is called ds then
#   atmospheric values come back as structure pieces in what looks like a 
#   data dictionary.  Here is the call to get the structure
#ds = ussa1976.compute()
#   or here is a call to get the data over a specific data range
ds = ussa1976.compute(z=np.arange(0.0, 40001.0, 1.0))
#   where the first value is the lower altitute, the second is the upper altitude
#   and the third is the altitude increment. The units seem to be meters.

# to get the data, you call the dictionary with the name of the 
z=ds["z"].values
p=ds["t"].values

#plt.figure(dpi=100)
#ds.p.plot(y="z", xscale="log")
#plt.grid()
plt.figure()
plt.plot(p,z)
plt.show()


#Here are the data dictionary names to use to get the data pieces
# Symbol Variable name
#
#t air temperature
#p air pressure
#n number density
#n_tot air number density
#rho air density
# mv air molar volume 
#hp air pressure scale height
#v air particles mean speed
#mfp air particles mean free path
#f air particles mean collision frequency
#cs speed of sound in air
#mu air dynamic viscosity
#nu air kinematic viscosity
#kt air thermal conductivity coefficient