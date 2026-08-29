from src.database.connection import get_connection
from datetime import datetime
from zoneinfo import ZoneInfo

def insert_stock_metric(df):

    df.columns = df.columns.str.strip()
    
    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
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
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (
                df['TICKER'],
                df['PRECO'],
                df['DY'],
                df['P/L'],
                df['P/VP'],
                df['ROE'],
                df['LIQUIDEZ MEDIA DIARIA'],
                df['DIV. LIQ. / PATRI.'],
                df['CAGR RECEITAS 5 ANOS'],
                datetime.now(ZoneInfo("America/Sao_Paulo"))
            ))

