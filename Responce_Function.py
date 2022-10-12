import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as sp
import scipy.fft as fft


def Refractive_index(w, w_TO, w_LO, gamm, epsilInf):

	n_w = np.sqrt(1+((w_LO**2-w_TO**2)/(w_TO**2-(sp.hbar*w)**2-1j*sp.hbar*w*gamm))*epsilInf)

	return n_w

def Complex_function(n_w, c, thickness, w, n_g):

	G_w = 2/((n_w+1)*((c*np.exp(-1j*2*sp.pi*w*thickness*(n_g-n_w)/c)-1)/(-1j*2*sp.pi*w*thickness*(n_g-n_w))))
	
	return G_w

def Electrooptic_Coeff(r_e, w, w_TO, gamm, Faust_Henry_coeff):

	r41_w = r_e*(1+Faust_Henry_coeff*(1-((sp.hbar*w)**2-1j*sp.hbar*w*gamm)/w_TO**2)**(-1))

	return r41_w

##  Documentation

# w (0 to 100 THz) (10**12)
# w_TO 
# w_LO
# gamm
# epsilInf
# sp.hbar
# n_w
# c
# thickness (1:50)*10**(-6)m
# n_g (800 nm)
# sp.pi
# Faust_Henry_coeff 
# r_e


#constants

w_TO = 177
w_LO = 206
gamm = 3.01
epsilInf = 6.7
Faust_Henry_coeff = -0.07**(0.02)


n_g = 3.224 ###########
r_e = 1 ########
c = 1 #############



for i in range(1,101):


	thickness = i
	w = np.linspace(1, 100, 100)



	n_w = Refractive_index(w, w_TO, w_LO, gamm, epsilInf)
	Comp_F = Complex_function(n_w, c, thickness, w, n_g)
	Electro_Coeff = Electrooptic_Coeff(r_e, w, w_TO, gamm, Faust_Henry_coeff)

	ComplexResponse_function = Complex_function(n_w, c, thickness, w, n_g)*Electrooptic_Coeff(r_e, w, w_TO, gamm, Faust_Henry_coeff)


	fig = plt.figure()
	ax = fig.add_subplot()
	plt.title(str(i)+' micrometers')
	ax.semilogy(w, abs(fft.fft(Comp_F)))
	name = str(i)+'.png'
	plt.savefig(name)

images = []
for i in range(1,101):
	images.append(imageio.imread(str(i)+'.png'))
imageio.mimsave('movie.gif', images)

# plt.plot(w, abs(1/Comp_F))
# plt.show()


