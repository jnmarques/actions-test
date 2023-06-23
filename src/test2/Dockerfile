FROM python:3.11-slim

WORKDIR /usr/src/app

COPY src/test2/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/test2 .

CMD [ "python", "-u" ,"test2.py" ]