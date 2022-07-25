FROM python:latest

ARG SSL_KEYFILE
ARG SSL_CERTFILE
ARG API_PORT=8000
ARG API_ADDRESS=127.0.0.1

ENV MONGO_ADDRESS=127.0.0.1
ENV MONGO_PORT=27017

WORKDIR /home

COPY . .

RUN pip install uvicorn

CMD [ "python", "uvicorn", "main:app", "--host=${API_ADDRESS}", "--port=${API_PORT}", "--ssl-keyfile=${SSL_KEYFILE}", "--ssl-certfile=${SSL_CERTFILE}"]

EXPOSE ${API_PORT}