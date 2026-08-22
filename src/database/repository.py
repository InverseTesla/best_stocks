from src.database.connection import get_connection


def insert_stock_metric():
    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                INSERT INTO stock_metrics (
                    ticker,
                    collected_at,
                    dividend_yield,
                    price_to_earnings,
                    price_to_book,
                    roe
                )
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (
                "PETR4",
                "2026-08-22 20:00:00",
                12.50,
                5.20,
                1.10,
                21.30,
            ))