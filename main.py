from src.utils.logger import logger
from src.core.extract import extract_data
from src.core.filter import filter_dataframe
from src.core.transform import transform_data
from src.core.send_email import send_email
from src.database.schema import create_tables
from src.database.repository import insert_stock_metric

try:
    logger.info("Iniciando execução.")

    create_tables()

    df = extract_data()

    insert_stock_metric(df)

    df = filter_dataframe(df)

    series = transform_data(df)

    send_email(series)

    logger.info("Execução finalizada.")
except Exception as e:
    logger.error("Erro ao executar pipeline: %s.", e)

