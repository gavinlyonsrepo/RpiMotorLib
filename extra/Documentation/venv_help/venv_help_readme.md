### Virtual Environment (recommended)

Using a virtual environment keeps the installation isolated and avoids
conflicts with system packages. To create and activate one:
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install rpimotorlib[rpilgpio]
```

To test the installation, copy an example script from the
`examples/` folder of the repository into your working directory
and run it:
```sh
# Example — download and run a DC motor test
wget https://raw.githubusercontent.com/gavinlyonsrepo/RpiMotorLib/master/examples/dc_motors/L298_DCMot_Test.py
python3 L298_DCMot_Test.py
```

Or clone the full repo to get all examples:
```sh
git clone https://github.com/gavinlyonsrepo/RpiMotorLib.git
cd RpiMotorLib/examples/dc_motors
python3 L298_DCMot_Test.py
```

To deactivate when finished:
```sh
deactivate
```
