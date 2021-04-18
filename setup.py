from setuptools import setup

setup(
    name="rpimotorlib",
    version="3.0",
    author="Gavin Lyons",
    author_email="glyons66@hotmail.com",
    description="A python 3 library for various motors and servos to connect to a raspberry pi",
    long_description="""# python 3 library\n for various motors and servos\n to connect to a raspberry pi\n""",
    long_description_content_type="text/markdown",
    license="GPL",
    keywords="TB6612FNG L9110S DRV8833 A3967 L298 servo motor library raspberry pi 28BYJ-48 A4988 stepper DRV8825",
    url="https://github.com/gavinlyonsrepo/RpiMotorLib",
    download_url='https://github.com/gavinlyonsrepo/RpiMotorLib/archive/3.0.tar.gz',
    packages=['RpiMotorLib'],
    data_files=[('', ['README.md'])],
    install_requires=['pip'],
    setup_requires=['pip'],
    scripts=['RpiMotorLib/RpiMotorScriptLib.py'],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
