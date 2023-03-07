. dev/scripts/sh/source.sh

convert() {
    python src/main.py $1
}

menu() {
    if [[ $# != 0 ]]; then
        if type "menu_$1" >/dev/null 2>&1; then
            cmd=$1
            shift
            "menu_$cmd" "$@"
        else
            pyenv/bin/python -c "from dev.scripts.py.main import main;main('$1')"
        fi
    else
        pyenv/bin/python -c "from dev.scripts.py.main import main;main()"
    fi
}