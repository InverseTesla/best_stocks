import pandas
import io

def transform_data(data):

    csv_data = io.StringIO(data)

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
            'CAGR RECEITAS 5 ANOS',
            'CAGR LUCROS 5 ANOS',
            ' VPA',
            ' LPA',
            ' PEG Ratio'
            ]
            )

    ticker_name = df['TICKER'].str[:4]
    non_duplicates_mask = ~ticker_name.duplicated(keep='first')
    df_cleaned = df[non_duplicates_mask]

    print(df_cleaned)