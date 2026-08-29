from src.database.connection import get_connection

def create_stock_metrics_table(cur):

    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_metrics (
                
            id BIGSERIAL PRIMARY KEY,

            ticker VARCHAR(10) NOT NULL,

            price NUMERIC(10,4),

            dividend_yield NUMERIC(10,4),

            price_to_earnings NUMERIC(10,4),

            price_to_book NUMERIC(10,4),

            roe NUMERIC(10,4),

            daily_liquidity NUMERIC(15,4),

            debt_to_equity NUMERIC(10,4),

            annual_recurring_revenue NUMERIC(10,4),

            collected_at TIMESTAMPTZ NOT NULL
        );
        
    """)

def create_tables():

    with get_connection() as conn:

        with conn.cursor() as cur:

            create_stock_metrics_table(cur)