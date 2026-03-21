# tests/conftest.py
"""
Shared pytest configuration.
Stubs out all GPIO-related modules so tests run on any machine without hardware.
"""
import sys
from unittest.mock import MagicMock

# Stub hardware modules before any RpiMotorLib import touches them
sys.modules.setdefault("RPi", MagicMock())
sys.modules.setdefault("RPi.GPIO", MagicMock())
sys.modules.setdefault("lgpio", MagicMock())
sys.modules.setdefault("pigpio", MagicMock())
