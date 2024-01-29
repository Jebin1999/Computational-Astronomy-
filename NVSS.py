#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:56:05 2023

@author: jebin
"""

from astroquery.skyview import SkyView
import matplotlib.pyplot as plt
from astropy.wcs import WCS
import numpy as np

# Set the coordinates for the radio source
ra = 83.6331
dec = 22.0145

# Define the radio telescope and survey
telescope = 'TESS'  # e.g., 'NVSS' for NRAO VLA Sky Survey
survey = '1.4 GHz'  # e.g., '1.4 GHz' for 1.4 GHz frequency

# Query and retrieve the radio data
image_list = SkyView.get_images(position=f"{ra}, {dec}", survey=telescope, coordinates="J2000",
                                pixels="1000,1000", scaling="Log", grid=False)

# Extract the radio image data and WCS information
image_data = image_list[0][0].data
wcs = WCS(image_list[0][0].header)

# Plot the radio image
fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(projection=wcs)
ax.imshow(image_data, origin='lower', cmap='prism')
ax.set_xlabel('Right Ascension (J2000)')
ax.set_ylabel('Declination (J2000)')
ax.set_title(f"{telescope} {survey} Radio Image")
ax.coords.grid(color='white', linestyle='solid', alpha=0.5)
plt.colorbar(ax.images[0], label='Flux Density (Jy/beam)')
plt.show()

# Perform scientific analysis on the radio image data
# Calculate the total flux within a circular region of interest
center_x = 500
center_y = 500
radius = 200

region_data = image_data[center_y-radius:center_y+radius+1, center_x-radius:center_x+radius+1]
total_flux = region_data.sum()

print(f"Total flux within the circular region: {total_flux} Jy")
