from database.connection import get_connection

def create_stock_metrics_table(cur):

    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_metrics (
                
            id BIGSERIAL PRIMARY KEY,

            ticker VARCHAR(10) NOT NULL,

            collected_at TIMESTAMP NOT NULL,

            dividend_yield NUMERIC(10,4),

            price_to_earnings NUMERIC(10,4),

            price_to_book NUMERIC(10,4),

            roe NUMERIC(10,4)
        );
        
    """)

def create_tables():

    with get_connection() as conn:

        with conn.cursor() as cur:

            create_stock_metrics_table(cur)