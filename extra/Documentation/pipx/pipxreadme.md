# pipx Installation

As of PEP 668, users on many systems will get an error if they try to install
packages system-wide with pip (`environment is externally managed`).
**pipx** installs packages globally into isolated virtual environments and
is a clean solution to this problem.

## Install rpimotorlib with pipx

**Recommended (all Pi models including Pi 5):**
```sh
pipx install rpimotorlib
pipx inject rpimotorlib rpi-lgpio
```

**Legacy (Pi 1-4 with RPi.GPIO):**
```sh
pipx install rpimotorlib
pipx inject rpimotorlib RPi.GPIO
```

> **Warning:** Do not inject both `rpi-lgpio` and `RPi.GPIO` into the same
> pipx venv — both provide the `RPi.GPIO` namespace and will conflict.

**Optional hardware PWM servo support (Pi 1-4 only):**
```sh
pipx inject rpimotorlib pigpio
```

## Importing from a pipx environment

When running your own scripts outside the pipx venv, Python may not be able
to find the installed package. Two solutions are provided as example scripts
in `examples/pipx_example/`.

### Method 1 — sys.path.insert (PIPXExample_1_ServoGPIOTest.py)

Append the pipx package location to `sys.path` before importing:

```python
import sys
# Adjust this path to match your username and Python version
sys.path.insert(0, '/home/<username>/.local/pipx/venvs/rpimotorlib/lib/python3.11/site-packages/RpiMotorLib')

from rpiservolib import SG90servo
```

The path format is:
```
/home/<username>/.local/pipx/venvs/rpimotorlib/lib/python<version>/site-packages/RpiMotorLib
```

### Method 2 — pipx shebang (PIPXExample_2_ServoGPIOTest.py)

Change the shebang line at the top of your script to point to the pipx
Python interpreter:

```python
#!/home/<username>/.local/pipx/venvs/rpimotorlib/bin/python
```

The shebang path can be found from the installed `rpimotorscript` file:
```sh
cat ~/.local/bin/rpimotorscript | head -1
```

This method uses the standard `from RpiMotorLib import ...` import syntax
with no `sys.path` manipulation needed.

## Finding your pipx venv path

```sh
pipx list --short
pipx environment
```
