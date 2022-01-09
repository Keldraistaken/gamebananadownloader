import json
import shutil
from datetime import datetime

import patoolib
import requests
import os

# PATH = "/home/csgoservers/serverfiles4/css/maps/"
PATH = "/home/dora/Desktop"


class GamebananaAPI:
    def __init__(self, mod_id):
        self.base_api = "https://gamebanana.com/apiv5/Mod/" + str(
            mod_id) + "?_csvProperties=_idRow,_sName,_aFiles,_aGame,_sName,_aPreviewMedia,_aSubmitter"

    def get_json(self):
        url = self.base_api
        try:
            r = requests.get(self.base_api)
            j = json.loads(r.content)
            return j
        except:
            return []


def get_date(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)

    return dt_object


def download_file(url, local_filename, map_file):
    with requests.get(url, stream=True) as r:
        with open(map_file, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
            patoolib.extract_archive(map_file, outdir=PATH)
    os.remove(map_file)

    return local_filename
