#!/bin/sh
NODE_ENV=production &&
    (
        python -m pip install -r dev/constants/req.txt &
        ([ "$NODE_ENV" = "development" ] && rm -rf dist/ squashfs-root/ tmp/ .AppImage) &
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
        cp dev/constants/version/0/0/scripts/op/.desktop ./tmp/python/md2pdf.desktop &
        echo "from src.cli import cli
cli()" >./tmp/python/main.py &
        cp dev/constants/version/0/0/scripts/op/AppRun ./tmp/python/AppRun &
        cp ./dev/raw_docs/assets/images/icons/logo-min.png ./tmp/python/logo.png &
        wait
    ) &&
    (
        cp dev/constants/version/0/0/scripts/op/AppRun ./tmp/python/AppRun
        ./tmp/tool.AppImage ./tmp/python ./tmp/md2pdf.AppImage
        exit 0
    ) &&
    (
        [ "$NODE_ENV" = "development" ] && (
            cp ./tmp/md2pdf.AppImage ./.AppImage
        )
        exit 0
    ) &&
    exit 0
