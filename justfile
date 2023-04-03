# regex to match recipe names and their comments:
# ^    (?P<recipe>\S+)(?P<args>(?:\s[^#\s]+)*)(?:\s+# (?P<docs>.+))*

# Constants
purple_msg := '\e[38;2;151;120;211m%s\e[0m'
time_msg := '\e[38;2;151;120;211m%s\e[0m: %.2fs\n'

# Derived Constants
cwd := `python -c 'import os;print(os.getcwd())'`
system_python := if os_family() == "windows" { "py.exe -3.10" } else { "python3.10" }
pyenv_dir := cwd + if os_family() == "windows" { "\\pyenv" } else { "/pyenv" }
pyenv_bin_dir := pyenv_dir + if os_family() == "windows" { "\\Scripts" } else { "/bin" }
python := pyenv_bin_dir + if os_family() == "windows" { "\\python.exe" } else { "/python3" }
pyenv_activate := pyenv_bin_dir + if os_family() == "windows" { "\\Activate.ps1" } else { "/activate" }

# Choose recipes
default:
    @ just -lu; printf '%s ' press Enter to continue; read; just --choose

# n1 - n2
[private]
minus n1 n2:
    @ python -c 'print(round({{n1}} - {{n2}}, 2))'

# Time commands
[private]
time msg err *cmd:
    #!/usr/bin/env bash
    printf '{{purple_msg}}: ' 'cmd'; printf '%s ' {{cmd}}; echo
    cs=$(date +%s.%N)
    if {{cmd}}; then
        printf '{{time_msg}}' '{{msg}}' "$(just minus $(date +%s.%N) $cs)"
    else
        printf '{{time_msg}}' '{{err}}' "$(just minus $(date +%s.%N) $cs)"
    fi

# Time commands without saying command name
[private]
time_nc msg err *cmd:
    #!/usr/bin/env bash
    cs=$(date +%s.%N)
    if {{cmd}}; then
        printf '{{time_msg}}' '{{msg}}' "$(just minus $(date +%s.%N) $cs)"
    else
        printf '{{time_msg}}' '{{err}}' "$(just minus $(date +%s.%N) $cs)"
    fi

[private]
[unix]
b64e file:
    base64 -w0 {{file}}

# Run Menu Commands
[private]
menu cmd:
    @ just time_nc '{{cmd}}' '{{cmd}} failed' {{python}} -c "\"from dev.scripts.py.main import main;main('{{cmd}}')\""

# Run Without Time
[private]
menu_wt cmd:
    @ {{python}} -c "\"from dev.scripts.py.main import main;main('{{cmd}}')\""

[private]
nio_dev:
    @ {{ python }} -m no_implicit_optional dev; exit 0

[private]
nio_src:
    @ {{ python }} -m no_implicit_optional src; exit 0

[private]
ruff:
    @ {{ python }} -m ruff check dev/scripts/py --fix; {{ python }} -m ruff check src --fix; exit 0

# Set up development environment
bootstrap:
    #!/usr/bin/env bash
    rm -rf poetry.lock
    if test ! -e pyenv; then
        {{ system_python }} -m venv pyenv
        source {{pyenv_activate}}
    fi
    {{ python }} -m pip install --upgrade pip
    {{ python }} -m pip install mkdocs mkdocs-material mkdocs-minify-plugin mkdocs-redirects poetry
    {{ python }} -m poetry install --with dev
    for i in $(ls -d dev/scripts/py/inst_mods/*/); do
        case $i in
            *"__pycache__"*) ;;
            *) {{python}} -m pip install -e "${i%%/}";;
        esac
    done
    {{ python }} -c "import pypandoc;pypandoc.pandoc_download.download_pandoc(targetfolder='{{pyenv_bin_dir}}',delete_installer=True)"
    {{ python }} -m pip cache purge

[private]
dev_prompt:
    @ echo Run the following command every time you open the terminal:;echo

# Activate development environment
[windows]
dev: dev_prompt
    @ cat dev/constants/dev/init-win.txt;echo

# Activate development environment
[linux]
[unix]
dev: dev_prompt
    @ cat dev/constants/dev/init-linux.txt;echo

# Activate development environment
[macos]
dev: dev_prompt
    @ cat dev/constants/dev/init-mac.txt;echo


# Generate documentation
docs: (menu "docs")

# Get program's version
ver: (menu "ver")

# Set the version manually
set_ver: (menu "set_ver")

# Bump version
bump: (menu "bump")

# Push to Github
push: (menu "push")

# Copy constants
cc: (menu "cc")

# Generate scripts
gs: (menu "gs")

# Test Build
[private]
__tb platform:
    #!/usr/bin/env python
    import yaml

    with open("version.yml") as f:
        VLS = yaml.safe_load(f)["ls"][:3]
    with open(
        f"dev/constants/version/{VLS[0]}/{VLS[1]}/scripts/op/build_{{platform}}.sh",
    ) as f:
        print(f.read().replace("ENV=production", "ENV=development"))

# Build
[private]
__build platform:
    #!/usr/bin/env python
    import yaml

    with open("version.yml") as f:
        VLS = yaml.safe_load(f)["ls"][:3]
    with open(
        f"dev/constants/version/{VLS[0]}/{VLS[1]}/scripts/op/build_{{platform}}.sh",
    ) as f:
        print(f.read())

[private]
_build type platform: gs
    #!/usr/bin/env bash

    if test ! -e pyenv; then
        just bootstrap
        source {{pyenv_activate}}
        just gs
    fi
    just "__{{type}}" "{{platform}}" | bash

# Test Build
[linux]
tb: (_build "tb" "linux")

# Build
[linux]
build: (_build "build" "linux")

# Build for PyPi
[linux]
pypi: (_build "build" "pypi")

# Lint codebase
lint:
    @ just time "     no_implicit_optional in dev" "     no_implicit_optional Failed" just nio_dev
    @ just time "     no_implicit_optional in src" "     no_implicit_optional Failed" just nio_src
    @ just time "        Markdown Files Formatted" "Formatting Markdown Files Failed" {{ python }} -m mdformat docs
    @ just time "          Python Files Formatted" "  Formatting Python Files Failed" {{ python }} -m black -q .
    @ just time "             Python Files Linted" "     Linting Python Files Failed" just ruff
