import requests

def extract_data():

    url = "https://statusinvest.com.br/category/AdvancedSearchResultExport"

    params = {
        "search": """{
            "dy":{"Item1":7,"Item2":14},
            "p_l":{"Item1":3,"Item2":10},
            "p_vp":{"Item1":0.5,"Item2":2},
            "roe":{"Item1":15,"Item2":30},
            "liquidezmediadiaria":{"Item1":100000,"Item2":null},
            "dividaliquidapatrimonioliquido":{"Item1":null,"Item2":0.9},
        }""",
        "CategoryType": 1
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/csv"
    }

    response = requests.get(url, params=params, headers=headers)


    return response.text
