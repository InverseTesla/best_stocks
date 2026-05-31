from src.utils.logger import logger
import pandas
import io

def transform_data(data):

    csv_data = io.StringIO(data)

    try:
        df = pandas.read_csv(csv_data, sep = ';')

        df = df.drop(
            columns=[
                'P/ATIVOS', 
                'MARGEM BRUTA', 
                'MARGEM EBIT', 
                'MARG. LIQUIDA', 
                'P/EBIT', 
                'EV/EBIT', 
                'DIVIDA LIQUIDA / EBIT', 
                'PSR', 
                'P/CAP. GIRO', 
                'P. AT CIR. LIQ.', 
                'LIQ. CORRENTE',
                'ROA',
                'ROIC',
                'PATRIMONIO / ATIVOS',
                'PASSIVOS / ATIVOS',
                'GIRO ATIVOS',
                ' VPA',
                ' LPA',
                ' PEG Ratio'
                ]
                )

        ticker_name = df['TICKER'].str[:4]
        non_duplicates_mask = ~ticker_name.duplicated(keep='first')
        df_cleaned = df[non_duplicates_mask]
        df_cleaned = df_cleaned.dropna(axis=0)

        df_cleaned.to_excel("relatorio.xlsx", index=False)

        return df_cleaned['TICKER']

    except Exception as e:
        logger.error("Falha ao transformar ao processar a tabela de indicadores: %s", e)
        return None


    