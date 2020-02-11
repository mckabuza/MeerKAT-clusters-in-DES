# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:04:57 2020

@author: Kabelo McKabuza
"""
from astropy.io import fits
from astropy.wcs import wcs
import astropy.table as atpy
import numpy as np
import pylab as plt
#import time
from matplotlib import rcParams

rcParams['font.family'] = 'Courier New'
rcParams['font.size'] = '16'
#starttime = time.time()

image_file = 'AdvACT_y3a2_footprint_griz_1exp_v2.0.fits'
tab=atpy.Table().read('legacySurvey.fits')
tab1=atpy.Table().read('tankshape.csv')

hdu_list = fits.open(image_file)
data = hdu_list[1].data

w = wcs.WCS(hdu_list[1].header, hdu_list)

px, py = w.all_world2pix(tab.field(3), tab.field(4), 1)
px1, py1 = w.all_world2pix(tab1.field(0), tab1.field(1), 1)

y = []
for i in py:
    res = round(i)
    result = int(res)
    y.append(result)

x = []
for j in px:
    res1 = round(j)
    result1 = int(res1)
    x.append(result1)
   
array = data[y,x]

mask_indices = np.where(array == 1)
outside_clusters = np.where(array < 0)

plt.plot(px1, py1, color = 'black')
plt.scatter(px[mask_indices], py[mask_indices], s = 20, color = 'red', label = 'MeerKAT clusters in the DES footprint')
plt.scatter(px[outside_clusters], py[outside_clusters], s = 20, color = 'blue')
plt.legend(loc='upper right', fontsize = 15)
plt.axis([0,45000, -4000,9000])

#endtime = time.time()
#timedif = endtime - starttime
#print(str("{0:.2f}".format(timedif)) + " seconds")
