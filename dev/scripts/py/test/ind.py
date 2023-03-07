from typing import Any

import yaml

from src.core.api import Provider

PROV = "dfl"


def clean_obj(obj: Any) -> dict:
    if isinstance(obj, list):
        return [clean_obj(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: clean_obj(v) for k, v in obj.items()}
    elif isinstance(obj, type):
        print(obj.__name__, type(obj))
        return clean_obj(obj.dict())
    else:
        return obj


def main():
    tr = {PROV: Provider(PROV).test()}

    def str_presenter(dumper, data):
        """configures yaml for dumping multiline strings
        Ref: https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data
        """
        if data.count("\n") > 0:
            return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
        return dumper.represent_scalar("tag:yaml.org,2002:str", data)

    yaml.add_representer(str, str_presenter)

    for pk, pv in {i: tr[i] for i in sorted(tr)}.items():
        print(f"{pk}: {'✔' if pv['successful'] else '✘'}")
        if notes := pv.get("notes"):
            print("\n         ".join(("  notes: " + notes).split("\n")))
        print(f"  ping: {'✔ ({} ms)'.format(pv['ping']) if pv['ol'] else '✘'}\n  test:")
        for k, v in pv["test"].items():
            print(f"    {k}: {'✔' if v['successful'] else '✘'}")
            if st := v.get("stack trace"):
                print("      " + "\n      ".join(st.split("\n")))

    tr = clean_obj(tr)

    with open("tr.yml", "w") as f:
        yaml.dump(tr, f, indent=2, allow_unicode=True, sort_keys=False)


if __name__ == "__main__":
    main()
