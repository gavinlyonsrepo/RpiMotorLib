from setuptools import setup

setup(
    name="rpimotorlib",
    version="1.1",
    author="Gavin Lyons",
    author_email="glyons66@hotmail.com",
    description="A python 3 library for various motors and servos to connect to a raspberry pi",
    license="GPL",
    keywords="servo motor library raspberry pi SG90 28BYJ48 stepper gavin lyons ",
    url="https://github.com/gavinlyonsrepo/RpiMotorLib",
    download_url='https://github.com/gavinlyonsrepo/RpiMotorLib/archive/1.1.tar.gz',
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