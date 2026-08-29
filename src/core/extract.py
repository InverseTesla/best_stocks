from src.utils.logger import logger
from pathlib import Path
import requests
import tomllib
import pandas
import json
import io

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
        for chave, _ in config.items():
            search_dict[chave] = {
                "Item1": None,
                "Item2": None
            }

        params = {
            "search": json.dumps(search_dict),
            "CategoryType": 1
        }
            
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/csv"
        }

        response = requests.get(url, params=params, headers=headers, timeout=30)

        response.raise_for_status()

        logger.info("Indicadores consultados com sucesso.")

        csv_data = io.StringIO(response.text)
        
        df = pandas.read_csv(csv_data, sep=';', decimal=',', thousands='.')
        
        return df
    
    except requests.exceptions.RequestException as e:
        logger.error("Erro ao consultar os indicadores das empresas: %s", e)
        return None

if __name__ == "__main__":
    result = extract_data()
    print(result)