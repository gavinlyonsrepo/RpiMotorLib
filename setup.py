from setuptools import setup

setup(
    name="rpi_tempmon.py",
    version="1.4",
    author="gavin lyons",
    author_email="glyons66@hotmail.com",
    description="Display the ARM CPU and GPU temperature of Raspberry Pi",
    license=" GPL",
    keywords="PI Raspberry CPU ARM GPU,temperature",
    url="https://github.com/gavinlyonsrepo/raspeberrypi_tempmon",
    download_url='https://github.com/gavinlyonsrepo/raspeberrypi_tempmon/archive/1.4.tar.gz',
    packages=['rpiTempSrc','rpiTempMod',],
    install_requires= ['matplotlib','pip'],
    setup_requires = ['pip'],
    scripts=['rpiTempSrc/rpi_tempmon.py'],
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
