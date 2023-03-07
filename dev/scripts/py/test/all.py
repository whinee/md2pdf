from multiprocessing.pool import ThreadPool
from typing import Any

import yaml
from hyaku.api.providers import Provider

tr = {}

with open("constants/0/0/providers.yml", "r") as f:
    PROV_LS = yaml.safe_load(f.read())["providers"].keys()


def dcd(o: Any) -> dict:
    if isinstance(o, list):
        return [dcd(i) for i in o]
    elif isinstance(o, dict):
        return {k: dcd(v) for k, v in o.items()}
    elif isinstance(o, str):
        return o
    else:
        return o.dict()


def _test(prov: str):
    tr[prov] = Provider(prov).test()


with ThreadPool(20) as pool:
    pool.starmap(
        _test,
        [
            [
                i,
            ]
            for i in PROV_LS
        ],
    )
    pool.close()
    pool.join()

for pk, pv in {i: tr[i] for i in sorted(tr)}.items():
    print(f"{pk}: {'✔' if pv['successful'] else '✘'}")
    if notes := pv.get("notes"):
        print("\n         ".join(("  notes: " + notes).split("\n")))
    if not pv["successful"]:
        print(f"  ping: {'✔ ({} ms)'.format(pv['ping']) if pv['ol'] else '✘'}\n  test:")
        for k, v in pv["test"].items():
            print(f"    {k}: {'✔' if v['successful'] else '✘'}")

for k, v in tr.items():
    for tk, tv in v["test"].items():
        if op := tv.get("output", None):
            tr[k]["test"][tk]["output"] = dcd(op)


def str_presenter(dumper, data):
    """configures yaml for dumping multiline strings
    Ref: https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data
    """
    if data.count("\n") > 0:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(str, str_presenter)

with open("tr.yml", "w") as f:
    yaml.dump(tr, f, indent=2)
