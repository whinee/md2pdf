. dev/scripts/sh/source.sh

m2p() {
    python src/main.py $1
}

menu() {
    if [[ $# != 0 ]]; then
        if type "menu_$1" >/dev/null 2>&1; then
            cmd=$1
            shift
            "menu_$cmd" "$@"
        else
            t "$1" "$1 failed" pyenv/bin/python -c "from dev.scripts.py.main import main;main('$1')"
        fi
    else
        t "menu" "menu failed" pyenv/bin/python -c "from dev.scripts.py.main import main;main()"
    fi
}