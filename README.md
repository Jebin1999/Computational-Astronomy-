# Radio Astronomy Image Analysis with Astroquery and Astropy

This repository contains Python scripts to analyze radio astronomy images using data from astronomical surveys such as **TESS** and **NVSS**. The scripts utilize `astroquery` for querying data, `astropy` for handling World Coordinate System (WCS) transformations, and `matplotlib` for visualization.

## Requirements

To run these scripts, you will need the following Python packages:

- `matplotlib`
- `astropy`
- `astroquery`
- `numpy`

You can install the required packages by running:

```bash
pip install matplotlib astropy astroquery numpy

Scripts Overview

1. Radio Image Query and Visualization: M51 Galaxy
This script retrieves and visualizes a radio image of the M51 Galaxy using the TESS telescope data.

Queries data from the TESS survey using astroquery.
Retrieves a FITS image and extracts both the image data and WCS information.
Visualizes the radio image in log scale with a WCS grid.
Usage

To run the script:

bash
Copy code
python m51_radio_image.py
Sample Output

The output includes:

A grayscale image of the M51 Galaxy.
WCS grid and axes labeled with RA (Right Ascension) and Dec (Declination).
Colorbar representing intensity in log scale.
2. Radio Image Query, Visualization, and Analysis: TESS Survey at RA=83.6331, Dec=22.0145
This script retrieves a radio image of a source located at RA=83.6331 and Dec=22.0145 using the TESS telescope and performs scientific analysis on the image.

Queries data from the TESS telescope using astroquery.
Extracts and displays a radio image with a prism colormap.
Performs flux calculation within a circular region of interest on the image.
Usage

To run the script:

bash
Copy code
python radio_flux_analysis.py
Sample Output

The output includes:

A colorful radio image using a prism colormap.
A WCS grid with labeled axes for Right Ascension and Declination.
The calculated total flux density in Jy (Jansky) within a circular region.
How to Use

Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/radio-astro-image-analysis.git
cd radio-astro-image-analysis
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Run any of the provided scripts using Python.
Contact

For any questions or issues, feel free to contact Jebin Larosh at your.email@example.com.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

bash
Copy code

### File Structure
```plaintext
radio-astro-image-analysis/
│
├── m51_radio_image.py      # Script for querying and visualizing M51 galaxy image
├── radio_flux_analysis.py  # Script for querying radio data and calculating flux
└── README.md               # Documentation







