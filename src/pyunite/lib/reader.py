""" The script that reads all files """
import glob
import os
import json

def get_file_list() -> list[str]:
    """
    Get the list of files to unite from pyunite.json
    This also means filtering the include and excludes
    """
    pyuniteJson = json.loads(open(os.getcwd() + "/pyunite.json", "r").read())

    include = pyuniteJson["files"]
    exclude = pyuniteJson["exclude"]

    included = []
    excluded = []

    for filePattern in include:
       included.extend(glob.glob(filePattern, recursive=True, include_hidden=True, root_dir=os.getcwd()))

    for filePattern in exclude:
        excluded.extend(glob.glob(filePattern, recursive=True, include_hidden=True, root_dir=os.getcwd()))

    for file in excluded:
        while file in included:
            included.remove(file)
