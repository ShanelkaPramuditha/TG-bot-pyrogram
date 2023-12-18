FROM python:3.9-alpine

ADD . .

RUN pip install pyrogram==0.17.1

CMD ["python", "./bot.py"]