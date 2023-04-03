# Remove-Item dist\ -Recurse -Force
# Remove-Item tmp\ -Recurse -Force
python -m pip install -r dev\constants\req.txt
yarn

New-Item -itemtype Directory -path 'tmp\python'
Copy-Item -Path '{{project_name}}\**' -Destination 'tmp\' -recurse -Force
Set-Location tmp\
Invoke-WebRequest 'https://bootstrap.pypa.io/get-pip.py' -o get-pip.py
Set-Location python
Invoke-WebRequest 'https://www.python.org/ftp/python/{{python_ver}}.0/python-{{python_ver}}.0-embed-amd64.zip' -o python.zip
tar -xf python.zip
Remove-Item python.zip
Remove-Item python{{python_ver_nd}}._pth
Set-Location ..
.\python\python get-pip.py
Remove-Item get-pip.py
Set-Location ..

.\tmp\python\python -m pip uninstall -y --no-cache-dir --disable-pip-version-check wheel
.\tmp\python\python -m pip install --no-warn-script-location --no-cache-dir --disable-pip-version-check --upgrade pip
.\tmp\python\python -m pip install --no-warn-script-location --no-cache-dir --disable-pip-version-check --ignore-installed -r requirements.txt