#!/usr/bin/env python
#encoding=utf8

import os, json

if __name__ == "__main__":
    settings = {}
    setting_file_name = "SETTINGS.json"
    wfd = open(setting_file_name, "w")
    settings["ROOT_PATH"] = os.getcwd() + "/"

    # Configuration

    # Write to file
    json.dump(settings, wfp, sort_keys=True, indent=4)
