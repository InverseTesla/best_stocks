from src.utils.logger import logger


def transform_data(df):

    try:
        
        ticker_name = df['TICKER'].str[:4]
        non_duplicates_mask = ~ticker_name.duplicated(keep='first')
        df_cleaned = df[non_duplicates_mask]
        df_cleaned = df_cleaned.dropna(axis=0)

        df_cleaned.to_excel("relatorio.xlsx", index=False)

        logger.info("Filtragem aplicada na tabela de indicadores.")

        return df_cleaned['TICKER']

    except Exception as e:
        logger.error("Falha ao processar a tabela de indicadores: %s", e)
        return None


    