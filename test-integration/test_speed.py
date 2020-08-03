import pandas as pd
import urllib.parse
import requests
from tqdm import tqdm


SERVER_URL = "http://dorresteintesthub.ucsd.edu:6541"
#SERVER_URL = "http://mingwangbeta.ucsd.edu:6541"

def test_speed():
    df = pd.read_csv("test.tsv", sep=",")

    for i in tqdm(range(1000)):
        for entry in df.to_dict(orient="records"):
            smiles = str(entry["smiles"])
            if len(smiles) > 5:
                request_url = "{}/classify?smiles={}".format(SERVER_URL, urllib.parse.quote(smiles))
                r = requests.get(request_url)
                classification = r.json()