from setuptools import setup
import os
 
setup(
    name='exoplasim',
    version='3.1.6',
    packages=['exoplasim',],
    zip_safe=False,
    install_requires=["numpy>=1.16,<1.22","matplotlib","scipy"],
    extras_require = {"netCDF4": ["netCDF4"],
                      "HDF5": ["h5py"],
                      "petitRADTRANS": ["petitRADTRANS>=2.4"]},
    include_package_data=True,
    exclude_package_data={'': ['exoplasim/cat*',
                               'exoplasim/Cat_UG_00',
                               'exoplasim/glacier',
                               'exoplasim/images',
                               'exoplasim/octave',
                               'exoplasim/Plasim_Report',
                               'exoplasim/Plasim_RM_16', 
                               'exoplasim/Plasim_UG_16',
                               'exoplasim/puma',
                               'exoplasim/Puma_UG_17',
                               'exoplasim/ug_cat_00',
                               'exoplasim/sam',
                               'exoplasim/lsg',
                               'exoplasim/tools',
                               'exoplasim/plasim/run/*.sra']},
    author='Adiv Paradise',
    author_email='paradise.astro@gmail.com',
    license='GNU General Public License',
    license_files=["LICENSE.TXT",],
    url='https://github.com/alphaparrot/ExoPlaSim',
    description='Exoplanet GCM',
    long_description_content_type='text/x-rst',
    long_description=open('README.rst').read(),
    )
