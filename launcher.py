# -*- coding: utf-8 -*-

import json
import os
from subprocess import CalledProcessError


def launch():
    try:
        with open("config.json") as f:
            config = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        with open("config.json", "w") as f:
            model = {"token": "", "default_prefix": "$", "description": ""}

            json.dump(model, f, indent=4)

        with open("config.json") as f:
            config = json.load(f)

        print("Please enter configuration parameters.")

    if config["token"] is "":
        config["token"] = input("TOKEN: ")

    if config["description"] is "":
        config["description"] = input("DESCRIPTION: ")

    with open("config.json", "w+") as f:
        json.dump(config, f, indent=4)

    from bot import Sparks

    Sparks()


if __name__ == "__main__":
    launch()
