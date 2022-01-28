import requests as requests
import pandas as pd
import tabulate
from pandas import json_normalize

if __name__ == '__main__':
    session = requests.Session()

    hostname = "thecocktaildb.com"
    limit = 999
    auth = session.get('https://' + hostname)

    api_repos = f"/api/json/v1/1/random.php"
    # api_repos = f"/rest/api/1.0/projects/DIGITAL_OA/repos/aaiix_pa_pc_internalcookies_demo/browse?limit={limit}"
    response = session.get('https://' + hostname + api_repos)
    # print(response.json())
    values = response.json()
    df = json_normalize(values["drinks"])  # Results contain the required data
    print(df.to_markdown())
    #print(values)