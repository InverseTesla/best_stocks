from src.utils.logger import logger
from pathlib import Path
import tomllib
import pandas
import io


def filter_dataframe(df):

    ROOT_DIR = Path(__file__).resolve().parent.parent.parent

    try:
        with open(ROOT_DIR / "config.toml", "rb") as configs:
            config = tomllib.load(configs)
    except Exception as e:
        logger.error("Erro ao ler as configurações: %s", e)


    search_dict = {}
    for chave, valores in config.items():
        search_dict[chave] = {
            "Item1": None if valores["min"] == 0 else valores["min"],
            "Item2": None if valores["max"] == float("inf") else valores["max"]
        }

    column_config_map = {
        'dy': 'DY',
        'p_l': 'P/L',
        'p_vp': 'P/VP',
        'roe': 'ROE',
        'liquidezmediadiaria': 'LIQUIDEZ MEDIA DIARIA',
        'dividaliquidapatrimonioliquido': 'DIV. LIQ. / PATRI.',
        'receitas_cagr5': 'CAGR RECEITAS 5 ANOS'
    }

    
    df.columns = df.columns.str.strip()

    columns_to_keep = ['TICKER', 'PRECO']
    columns_to_keep.extend(list(column_config_map.values()))

    df = df[columns_to_keep]

    query_chunks = []
    for key, value in column_config_map.items():
        min_val = search_dict[key]['Item1']
        max_val = search_dict[key]['Item2']

        if min_val is not None and str(min_val).strip().lower() != 'none':
            query_chunks.append(f"`{value}` > {min_val}")

        if max_val is not None and str(max_val).strip().lower() != 'none':
            query_chunks.append(f"`{value}` < {max_val}")


    query = ' and '.join(query_chunks)

    filtered_df = df.query(query)

    return filtered_df