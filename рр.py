# import os
# import imageio
#
# png_dir='C:/Users/Admin/Desktop/Responce Function'
# images = []
# for file_name in sorted(os.listdir(png_dir)):
#     if file_name.endswith('.png'):
#         file_path = os.path.join(png_dir, file_name)
#         images.append(imageio.imread(file_path))
#
# # Make it pause at the end so that the viewers can ponder
# for _ in range(10):
#     images.append(imageio.imread(file_path))
#
# imageio.mimsave(images)

import numpy as np
import scipy.constants as sp

def Refractive_index(w, w_TO, w_LO, gamm, epsilInf):

    n_w = np.sqrt(1+((w_LO**2-w_TO**2)/(w_TO**2-(sp.hbar*w)**2-1j*sp.hbar*w*gamm))*epsilInf)
    return n_w


w_TO = 177
w_LO = 206
gamm = 3.01
epsilInf = 6.7

w = np.linspace(1, 100, 100)
print(len(Refractive_index(w, w_TO, w_LO, gamm, epsilInf)))
Comp_F = Complex_function(n_w, c, thickness, w, n_g)