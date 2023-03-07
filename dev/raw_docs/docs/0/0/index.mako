<%
    from os import path

    ver = '.'.join(cwd.split('/')[-2:])

    with open(path.join(cwd, "index.mmd"), "r") as f:
        md_op = f.read()
%><h1 align="center" style="font-weight: bold">
    ${ver}.x.x
</h1>

${md_op}