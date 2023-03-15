. "$XDG_CONFIG_HOME"/bash/source.sh

# commands

menu_fmt() { (
    t "          no_implicit_optional" "   no_implicit_optional Failed" LIBCST_PARSER_TYPE=native no_implicit_optional dev
    LIBCST_PARSER_TYPE=native t "          no_implicit_optional" "   no_implicit_optional Failed" no_implicit_optional src
    t "         Python Imports Sorted" " Sorting Python Imports Failed" isort -q --gitignore . &
    t "            Markdown Formatted" "    Formatting Markdown Failed" mdformat docs &
    t "        Python Files Formatted" "Formatting Python Files Failed" black -q . &
    wait
); }

menu_req() {
    pyenv/bin/python -m pip install --upgrade pip niet
    for i in $(
        for j in $(niet development.venv.requirements dev/vars.yml); do
            niet requirements."$j" dev/vars.yml
        done
    ); do
        pyenv/bin/python -m pip install -r "$i"
    done
    pyenv/bin/python -c "import pypandoc;pypandoc.pandoc_download.download_pandoc(targetfolder='$PWD/pyenv/bin',delete_installer=True)" &
    for i in $(ls -d dev/scripts/py/inst_mods/*/); do
        case $i in
        *"__pycache__"*) ;;
        *)
            pyenv/bin/python -m pip install -e "${i%%/}"
            ;;
        esac
    done &
    wait
}

menu_pt() {
    pyenv/bin/python <"dev/scripts/py/test/$1.py"
}

# main

if type "menu_$1" >/dev/null 2>&1; then
    cmd=$1
    shift
    "menu_$cmd" "$@"
else
    echo "menu: $1 is not in the menu."
fi
