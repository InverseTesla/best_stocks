from src.database.connection import get_connection
from src.utils.logger import logger
from datetime import datetime
from zoneinfo import ZoneInfo

def insert_stock_metric(df):

    try:
        df.columns = df.columns.str.strip()
        now = datetime.now(ZoneInfo("America/Sao_Paulo"))

        data_to_insert = [
            (
                row['TICKER'], 
                row['PRECO'], 
                row['DY'], 
                row['P/L'], 
                row['P/VP'],
                row['ROE'], 
                row['LIQUIDEZ MEDIA DIARIA'], 
                row['DIV. LIQ. / PATRI.'],
                row['CAGR RECEITAS 5 ANOS'],
                now
            )
            for _, row in df.iterrows()
        ]

        with get_connection() as conn:
            with conn.cursor() as cur:

                query = """
                    INSERT INTO stock_metrics (
                        ticker,
                        price,
                        dividend_yield,
                        price_to_earnings,
                        price_to_book,
                        roe,
                        daily_liquidity,
                        debt_to_equity,
                        annual_recurring_revenue,
                        collected_at
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                cur.executemany(query, data_to_insert)
                
                conn.commit()
    except Exception as e:
        logger.error("Erro ao inserir dados no banco: %s", e)

