import os
import smtplib
from datetime import date
from src.utils.logger import logger
from email.message import EmailMessage

def send_email(df):
    today = date.today()

    current_year = today.year
    last_year = current_year - 1

    first_quarter = date(current_year, 5, 16)
    second_quarter = date(current_year, 8, 16)
    third_quarter = date(current_year, 11, 16)
    fourth_quarter = date(current_year, 4, 1)

    current_quarter = None

    if today >= fourth_quarter and today < first_quarter:
        current_quarter = f"Quarto trimestre de {last_year}"
    elif today >= first_quarter and today < second_quarter:
        current_quarter = f"Primeiro trimestre de {current_year}"
    elif today >= second_quarter and today < third_quarter:
        current_quarter = f"Segundo trimestre de {current_year}"
    else:
        current_quarter = f"Terceiro trimestre de {current_year}"


    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    APP_PASSWORD = os.getenv("APP_PASSWORD")
    RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

    if not all([SENDER_EMAIL, APP_PASSWORD, RECEIVER_EMAIL]):
        logger.critical("Variáveis de ambiente obrigatórias não encontradas.")
        raise RuntimeError("Configuração inválida")


    msg = EmailMessage()

    tickers_html = "<ul>"

    tickers_html = "".join(
        f"<li>{ticker}</li>"
        for ticker in df
    )

    tickers_html = f"<ul>{tickers_html}</ul>"


    html = f"""
    <html>

    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>

    body {{
        font-family: Arial, sans-serif;
        background-color: #f4f6f9;
        padding: 30px;
    }}

    .container {{
        background-color: white;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }}

    h1 {{
        color: #111827;
        margin-bottom: 5px;
    }}

    .subtitle {{
        color: #6b7280;
        margin-bottom: 30px;
    }}

    .date {{
        float: right;
        color: #374151;
        font-weight: bold;
    }}

    table {{
        border-collapse: collapse;
        width: 100%;
        overflow: hidden;
        border-radius: 10px;
    }}

    th {{
        background-color: #0f172a;
        color: white;
        padding: 14px;
        text-align: center;
        font-size: 14px;
    }}

    td {{
        padding: 12px;
        border-bottom: 1px solid #e5e7eb;
        text-align: center;
        font-size: 14px;
    }}

    tr:nth-child(even) {{
        background-color: #f9fafb;
    }}

    tr:hover {{
        background-color: #eef2ff;
    }}

    .footer {{
        margin-top: 25px;
        font-size: 12px;
        color: #6b7280;
    }}

    </style>
    </head>

    <body>

    <div class="container">

    <div class="date">
    {current_quarter}
    </div>

    <h1>📈 Melhores ações</h1>

    <div class="subtitle">
    Relatório fundamentalista automático
    </div>

    {tickers_html}

    <div class="footer">
    Dados calculados automaticamente com base nos filtros selecionados.
    </div>

    </div>

    </body>
    </html>
    """

    msg['Subject'] = f"Melhores ações | {current_quarter}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    
    msg.add_alternative(html, subtype='html')

    with open("relatorio.xlsx", "rb") as file:
        msg.add_attachment(
            file.read(),
            maintype = "application",
            subtype = "vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename = f"Relatório Completo do {current_quarter}.xlsx"
        )


    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
            logger.info("E-mail enviado com sucesso.")
            os.remove("relatorio.xlsx")
    except Exception as e:
       logger.error("Erro ao enviar e-mail: %s", e)
