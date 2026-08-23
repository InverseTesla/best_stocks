from src.utils.logger import logger
from src.core.extract import extract_data
from src.core.filter import filter_dataframe
from src.core.transform import transform_data
from src.core.send_email import send_email
#from src.database.schema import create_tables
#from src.database.repository import insert_stock_metric

logger.info("Iniciando execução.")

#create_tables()
#insert_stock_metric()

data = extract_data()

df = filter_dataframe(data)

series = transform_data(df)

send_email(series)

logger.info("Execução finalizada.")