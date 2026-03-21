"""
RpiMotorLib settings manager.
Reads/writes ~/.config/rpiMotorLib/config.ini
Creates the file with defaults if missing.
"""

import configparser
import logging
import os
from pathlib import Path

_log = logging.getLogger(__name__)

# === Paths ===
CONFIG_DIR  = Path.home() / ".config" / "rpiMotorLib"
CONFIG_FILE = CONFIG_DIR / "config.ini"

# === Defaults (written on first run) ===
DEFAULTS = {
    "gpio": {
        "backend": "null",   # null = auto-detect
    }
}

VALID_BACKENDS = {"null", "rpigpio", "lgpio"}


def _create_default_config() -> None:
    """Create config directory and file with default values."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    config = configparser.ConfigParser()
    for section, values in DEFAULTS.items():
        config[section] = values
    with CONFIG_FILE.open("w") as f:
        f.write("# RpiMotorLib configuration\n")
        f.write("# backend: null | rpigpio | lgpio\n")
        f.write("#   null    = auto-detect (recommended)\n")
        f.write("#   rpigpio = force RPi.GPIO / rpi-lgpio\n")
        f.write("#   lgpio   = force native lgpio\n\n")
        config.write(f)
    _log.info("Created default config: %s", CONFIG_FILE)


def load() -> configparser.ConfigParser:
    """Load config, creating defaults if the file doesn't exist."""
    if not CONFIG_FILE.exists():
        _create_default_config()
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config


def get_gpio_backend() -> str:
    """
    Return the configured GPIO backend.

    Priority:
        1. RPIMOTORLIB_GPIO_BACKEND environment variable (override)
        2. ~/.config/rpiMotorLib/config.ini  [gpio] backend
        3. 'null' (auto-detect)
    """
    # 1. environment variable takes highest priority
    env = os.environ.get("RPIMOTORLIB_GPIO_BACKEND", "").strip().lower()
    if env:
        _log.debug("GPIO backend from env var: %s", env)
        return env

    # 2. Config file
    config = load()
    backend = config.get("gpio", "backend", fallback="null").strip().lower()

    if backend not in VALID_BACKENDS:
        _log.warning(
            "Unknown backend '%s' in config, falling back to null. "
            "Valid options: %s", backend, VALID_BACKENDS
        )
        backend = "null"

    _log.debug("GPIO backend from config file: %s", backend)
    return backend
