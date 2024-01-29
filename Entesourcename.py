#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 16:03:50 2023

@author: jebin
"""
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astroquery.skyview import SkyView

# Define the source name and telescope
source_name = 'M51'
telescope = 'TESS'

# Query radio data
image_list = SkyView.get_images(position=source_name, survey=telescope, coordinates="J2000",
                                pixels="1000,1000", scaling="Log", grid=True)

# Get the FITS header and data
fits_header = image_list[0][0].header
image_data = image_list[0][0].data

# Create the WCS object
wcs = WCS(fits_header)

# Plot the image
plt.figure()
plt.imshow(image_data, origin='lower', cmap='gray', extent=wcs.calc_footprint().flatten())
plt.title(f'Radio Image of {source_name} ({telescope})')
plt.xlabel('RA (degrees)')
plt.ylabel('Dec (degrees)')
plt.colorbar(label='Intensity (log scale)')
plt.show()


