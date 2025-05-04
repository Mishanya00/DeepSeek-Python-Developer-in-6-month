import asyncio

from email.message import EmailMessage
from aiosmtplib import SMTP
from dotenv import dotenv_values


config = dotenv_values(".env")
EMAIL = config['EMAIL']
PASSWORD = config['PASSWORD']
APP_NAME= config['APP_NAME']
APP_PASSWORD = config['APP_PASSWORD']
RECEPIENT = config['RECEPIENT']

async def send_email(recepient: str):
    msg = EmailMessage()
    msg["From"] = EMAIL
    msg["To"] = recepient
    msg['subject'] = 'Python Automation'
    msg.set_content("Test asynchronous email from Python")

    async with SMTP(hostname="smtp.gmail.com", port=587) as smtp:
        # await smtp.starttls()
        await smtp.login(EMAIL, APP_PASSWORD)
        await smtp.send_message(msg)


asyncio.run(send_email(RECEPIENT))