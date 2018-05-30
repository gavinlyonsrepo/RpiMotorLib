from setuptools import setup

setup(
    name="rpimotorlib",
    version="2.1",
    author="Gavin Lyons",
    author_email="glyons66@hotmail.com",
    description="A python 3 library for various motors and servos to connect to a raspberry pi",
    license="GPL",
    keywords="servo motor library raspberry pi SG90 28BYJ-48 A4988 stepper DRV8825",
    url="https://github.com/gavinlyonsrepo/RpiMotorLib",
    download_url='https://github.com/gavinlyonsrepo/RpiMotorLib/archive/2.1.tar.gz',
    packages=['RpiMotorLib'],
    data_files=[('/usr/share/doc/rpimotorlib/', ['README.md'])],
    install_requires=['pip'],
    setup_requires=['pip'],
    scripts=['RpiMotorLib/RpiMotorScriptLib.py'],
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
