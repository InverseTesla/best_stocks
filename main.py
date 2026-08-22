from src.utils.logger import logger
from src.core.extract import extract_data
from src.core.transform import transform_data
from src.core.send_email import send_email
from src.database.schema import create_tables
from src.database.repository import insert_stock_metric

logger.info("Iniciando execução.")

create_tables()
insert_stock_metric()

data = extract_data()

logger.info("Indicadores consultados com sucesso.")

df = transform_data(data)

logger.info("Filtragem aplicada na tabela de indicadores.")

send_email(df)

logger.info("Execução finalizada.")

