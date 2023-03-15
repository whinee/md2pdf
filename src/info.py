import locale
import os
import platform
from os import path
from os.path import dirname, realpath
from shutil import get_terminal_size
from sys import platform as PLATFORM
from typing import Final

import msgpack

# Constants
DEF_STR = "c0VjUmVUX2NPZEUgYnkgd2hpX25l"

# Derived Constants

## Project Info

PROJ_ABS_PATH: Final[str] = dirname(realpath(__file__))

with open(path.join(PROJ_ABS_PATH, "constants", "const.mp"), "rb") as f:
    CONST = msgpack.unpackb(f.read(), raw=False, use_list=True)

PROJECT_NAME = CONST["project_name"]
"""Project's name"""

__version__ = CONST["ver"]
"""The current version of the project.

This project uses a modified semver. For more information, visit [this link](../../../notes-to-self.md#versioning-system).
"""

CHOLDER = CONST["cholder"]
"""HTML text of copyright holders of this project"""

SVER = CONST["sver"]
"""The current version of the project, compliant with the semver.

This project uses a modified semver. For more information, visit [this link](../../../notes-to-self.md#versioning-system).
"""

VLS = CONST["vls"]
"""The current version of the project as a list.

The list consists of 6 integers, which represent the following:
    - User
    - Dev
    - Minor
    - Patch
    - Prerelease Identifier
        The prerelease identifier number corresponds to the following values:
            0: alpha
            1: beta
            2: release candidate or rc
            3: none
    - Prerelease Version
"""

VARIANT = "package"
"""The application variant

This is useful for debugging, and for initializing the application's configuration.
Following are the allowed variants:

- `installable`: for when the application is packed as an installable application
- `package`: for when the application is published on PyPi (as a Python Library)
- `portable`: for when the application is packed as a portable application
"""

## Machine Info

try:
    TW = get_terminal_size().columns
    """Stands for terminal width.
    """
except OSError:
    TW = 0

MACHINE = platform.machine()

match PLATFORM:
    case "win32":
        PSH = "win"
        """Platform Short Hand"""
    case "darwin":
        PSH = "mac"
    case _:
        PSH = PLATFORM

match PLATFORM:
    case "win32":
        import ctypes

        LOCALE = locale.windows_locale[
            ctypes.windll.kernel32.GetUserDefaultUILanguage()
        ][:2]

        CFLOP: Final[list[str]] = [
            rf"{os.getcwd()}\{PROJECT_NAME}.yml",
            rf'{os.getenv("USERPROFILE")}\AppData\Roaming\{PROJECT_NAME}\config.yml',
        ]
        """
        Stands for `Configuration File Lookup Order of Precedence`

        List of paths to look for the configuration file at.

        ```mermaid
        flowchart LR
            A([Config]) --> B[Grab CFLOP]
            B --> C{Last item}
                C --> |false| D{File exists?}
                    D --> |true| E([Read config file])
                    D --> |false| C
                C --> |true| F{OS?}
                    F --> |Windows| G[Initialize config file<br>at first lookup path] --> E
                    F --> |*nix| H{.AppImage?}
                        H --> |true| I[Initialize config file<br>at second lookup path] --> E
                        H --> |false| G
        ```
        """
    case "darwin" | "linux":
        if _LOCALE := locale.getdefaultlocale()[0]:
            LOCALE = _LOCALE[:2]  # type: ignore[misc, no-redef]
        else:
            LOCALE = "en"  # type: ignore[misc, no-redef]

        CFLOP = [  # type: ignore[misc]
            f"{os.getcwd()}/{PROJECT_NAME}.yml",
            "~/.config/{PROJECT_NAME}/config.yml",
            "~/.{PROJECT_NAME}",
        ]
        if xch := os.getenv("XDG_CONFIG_HOME"):
            CFLOP.insert(1, f"{xch}/{PROJECT_NAME}/config.yml")
        if _LOCALE := locale.getdefaultlocale()[0]:
            LOCALE: Final[str] = _LOCALE[:2]  # type: ignore[misc, no-redef]
    case _:
        raise Exception(f"Platform not Supported: {PLATFORM}")
