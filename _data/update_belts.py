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
        fetched_belts = belts(color, fetch=True)
        pre_existing_belts = belts(color, fetch=False)
        for belt in fetched_belts.values():
            belt["fetched"] = True
        return {**fetched_belts, **pre_existing_belts}

    yellow_belts = join("yellow")
    blue_belts = join("blue")

    for belt_id in blue_belts:
        blue_belt = blue_belts[belt_id]
        yellow_belt = yellow_belts[belt_id]
        upgraded = blue_belt.get("fetched") and not yellow_belt.get("fetched")
        if upgraded:
            upgrade_date = blue_belt["date"]
            blue_belts[belt_id] = yellow_belt.copy()
            blue_belts[belt_id]["date"] = upgrade_date

    yellow_belts = {k: v for k, v in yellow_belts.items() if k not in blue_belts}

    def clean(belts):
        for belt_id, belt in belts.items():
            original_belt = belt.copy()
            belt = {}
            order = ["handle", "date", "name", "emoji", "site", "mail"]
            for key in order:
                if original_belt.get(key):
                    belt[key] = original_belt[key]
            belts[belt_id] = belt

    clean(yellow_belts)
    clean(blue_belts)

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
