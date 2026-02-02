import pandas
import requests

url = "https://statusinvest.com.br/category/AdvancedSearchResultExport"

params = {
    "search": """{
        "dy":{"Item1":null,"Item2":null},
        "p_l":{"Item1":null,"Item2":null},
        "roe":{"Item1":null,"Item2":null}
    }""",
    "CategoryType": 1
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/csv"
}

r = requests.get(url, params=params, headers=headers)

with open("statusinvest_acoes.csv", "wb") as f:
    f.write(r.content)