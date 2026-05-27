import os
import smtplib
from datetime import date
from email.message import EmailMessage

def send_email(df):
    today = date.today()

    today_formatted = today.strftime("%d/%m/%Y")

    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    APP_PASSWORD = os.getenv("APP_PASSWORD")
    RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")


    msg = EmailMessage()

    html = f"""
    <html>

    <head>
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
    {today_formatted}
    </div>

    <h1>📈 Melhores ações</h1>

    <div class="subtitle">
    Relatório fundamentalista automático
    </div>

    {df.to_html(index=False)}

    <div class="footer">
    Dados calculados automaticamente com base nos filtros selecionados.
    </div>

    </div>

    </body>
    </html>
    """

    msg['Subject'] = f"Melhores ações | {today_formatted}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    msg.add_alternative(html, subtype='html')

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
            print("Successfully sent the mail.")
    except Exception as e:
        print(f"Error: {e}")
