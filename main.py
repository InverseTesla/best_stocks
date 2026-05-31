from utils.logger import logger
from core.extract import extract_data
from core.transform import transform_data
from core.send_email import send_email

logger.info("Iniciando execução.")
data = extract_data()

logger.info("Indicadores consultados com sucesso.")

df = transform_data(data)

logger.info("Filtragem aplicada na tabela de indicadores.")

send_email(df)

logger.info("Execução finalizada.")

