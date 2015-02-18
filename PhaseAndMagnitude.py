# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 19:33:09 2015

@author: bxiao
Here is a new comment
"""
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

# read in an image using mis. 
img = misc.imread('cheetah.png',flatten=1)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
# compute magnitude
magnitude_cheetah = np.abs(fshift)
# compute phase
phase_cheetah = np.angle(fshift)
# read in an image using mis. 
img2 = misc.imread('zebra.png',flatten=1)
f = np.fft.fft2(img2)
fshift = np.fft.fftshift(f)
# compute magnitude
magnitude_zebra = np.abs(fshift)
# compute phase
phase_zebra = np.angle(fshift)

# display the original image and the DFT components
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_cheetah, cmap = 'gray')
plt.title('Log Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(phase_cheetah, cmap = 'gray')
plt.title('Phase'), plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(131),plt.imshow(img2, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_zebra, cmap = 'gray')
plt.title('Log Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(phase_zebra, cmap = 'gray')
plt.title('Phase'), plt.xticks([]), plt.yticks([])
plt.show()

# reconstrution, please switch phase of zebra and cheeta, and display the final image here
# first, let's test whether we can put together the magnitude and the phase. 
#re = np.sqrt((magnitude_zebra**2)/np.sqrt(1+np.tan(phase_zebra)**2))
#im = re*np.tan(phase_zebra)
re = magnitude_zebra*np.cos(phase_zebra)
im = magnitude_zebra*np.sin(phase_zebra)
F = re+1j*im
f_ishift = np.fft.ifftshift(F)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
#img_back=  misc.bytescale(img_back)
print img_back.min(), img_back.max()
plt.imshow(np.uint8(img_back), cmap='gray')
plt.show()

# mismatch the phase of zebra and cheeta
theta = np.cos(phase_zebra)
re = magnitude_cheetah*theta
im = magnitude_cheetah*np.sin(phase_zebra)
F = re+1j*im
f_ishift = np.fft.ifftshift(F)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
img_back=  misc.bytescale(img_back)
print img_back.min(), img_back.max()
plt.imshow(np.uint8(img_back), cmap='gray')
plt.show()




