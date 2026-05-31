from pathlib import Path
from utils.logger import logger
import requests
import tomllib
import json

def extract_data():

    ROOT_DIR = Path(__file__).resolve().parent.parent.parent

    try:
        with open(ROOT_DIR / "config.toml", "rb") as configs:
            config = tomllib.load(configs)
    except Exception as e:
        logger.error("Erro ao ler as configurações: %s", e)


    try:
        url = "https://statusinvest.com.br/category/AdvancedSearchResultExport"

        search_dict = {}
        for chave, valores in config.items():
            search_dict[chave] = {
                "Item1": None if valores["min"] == 0 else valores["min"],
                "Item2": None if valores["max"] == float("inf") else valores["max"]
            }

        params = {
            "search": json.dumps(search_dict),
            "CategoryType": 1
        }
            
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "text/csv"
        }

        response = requests.get(url, params=params, headers=headers, timeout=30)

        response.raise_for_status()
        
        return response.text
    
    except requests.exceptions.RequestException as e:
        logger.error("Erro ao consultar os indicadores das empresas: %s", e)
        return None

if __name__ == "__main__":
    result = extract_data()
    print(result)