FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/test1 .

CMD [ "python", "-u" ,"test1.py" ]