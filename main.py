from src.extract import extract_data
from src.transform import transform_data
from src.send_email import send_email


data = extract_data()

df = transform_data(data)

send_email(df)

