#!/usr/bin/env python3

import pathlib
import datetime

import requests
import yaml

URL = "https://cse466.pwn.college"
DIR = pathlib.Path(__file__).parent


def belt_path(color):
    return DIR / f"{color}.yml"


def belts(color, fetch=False):
    if fetch:
        return requests.get(f"{URL}/pwncollege_api/v1/belts/{color}").json()
    else:
        path = belt_path(color)
        if not path.exists():
            return {}
        with open(path) as f:
            return yaml.load(f.read(), Loader=yaml.BaseLoader)


def main():
    def join(color):
        return {**belts(color, fetch=True), **belts(color)}

    yellow_belts = join("yellow")
    blue_belts = join("blue")

    yellow_belts = {k: v for k, v in yellow_belts.items() if k not in blue_belts}

    def sort(belts):
        return dict(
            sorted(
                belts.items(),
                key=lambda k: datetime.datetime.fromisoformat(k[1]["date"]),
            )
        )

    yellow_belts = sort(yellow_belts)
    blue_belts = sort(blue_belts)

    def output(color, belts):
        with open(belt_path(color), "w") as f:
            f.write(yaml.dump(belts, sort_keys=False))

    output("yellow", yellow_belts)
    output("blue", blue_belts)


if __name__ == "__main__":
    main()
