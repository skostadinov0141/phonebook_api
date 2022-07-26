FROM python:latest

WORKDIR /home

COPY . .

RUN pip install uvicorn
RUN pip install fastapi
RUN pip install pymongo

RUN mkdir keys

ENTRYPOINT [ "uvicorn", "main:app" ]

EXPOSE ${API_PORT}