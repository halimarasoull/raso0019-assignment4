FROM python:3.8

WORKDIR /usr/src/app

COPY README .

RUN pip install -r requirements.txt

COPY app.py .

CMD [ "python", "./app.py" ]