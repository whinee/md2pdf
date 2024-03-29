#!/usr/bin/env bash
ENV=production &&
    sudo apt install libfuse2 &&
    source pyenv/bin/activate &&
    (
        ([ "$ENV" = "development" ] && rm -rf dist/ squashfs-root/ tmp/ .AppImage) &
        wait
    ) &&
    mkdir tmp/ &&
    (
        wget -O ./tmp/python.AppImage "$(wget -qSO - "https://api.github.com/repos/niess/python-appimage/releases/tags/python3.10" 2>/dev/null | grep -E "browser_download_url.*x86_64" | cut -d '"' -f4 | tail -1)" >/dev/null &
        wget -O ./tmp/tool.AppImage https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage >/dev/null &
        wait
    ) &&
    (
        chmod +x ./tmp/tool.AppImage &
        chmod +x ./tmp/python.AppImage &
        wait
    ) &&
    ./tmp/python.AppImage --appimage-extract >/dev/null &&
    mv squashfs-root tmp/python/ &&
    (
        rm -f ./tmp/python.AppImage &
        rm -rf ./tmp/python/*.png &
        rm -rf ./tmp/python/*.desktop &
        cp -r src tmp/python &
        ./tmp/python/opt/python3.10/bin/python3.10 -m pip install --upgrade pip --no-warn-script-location --no-cache-dir --disable-pip-version-check &
        ./tmp/python/opt/python3.10/bin/python3.10 -m pip uninstall wheel -y --no-cache-dir --disable-pip-version-check &
        wait
    ) &&
    (
        ./tmp/python/opt/python3.10/bin/python3.10 -m pip install --no-warn-script-location --no-cache-dir --disable-pip-version-check -I -r requirements.txt &
        cp {{ver_dir}}/scripts/op/.desktop ./tmp/python/{{project_name}}.desktop &
        echo "from src.cli import cli
cli()" >./tmp/python/main.py &
        cp {{ver_dir}}/scripts/op/AppRun ./tmp/python/AppRun &
        cp ./dev/raw_docs/assets/images/icons/logo-min.png ./tmp/python/logo.png &
        wait
    ) &&
    (
        cp {{ver_dir}}/scripts/op/AppRun ./tmp/python/AppRun
        ./tmp/tool.AppImage ./tmp/python ./tmp/{{project_name}}.AppImage
        exit 0
    ) &&
    (
        [ "$ENV" = "development" ] && (
            cp ./tmp/{{project_name}}.AppImage ./.AppImage
        )
        exit 0
    ) &&
    exit 0
