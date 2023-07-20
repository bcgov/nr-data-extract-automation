#FROM oraclelinux:8-slim

FROM python:3.11.4-slim-buster

WORKDIR    /opt/oracle
RUN        apt-get update && apt-get install -y libaio1 wget unzip \
            && wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip \
            && unzip instantclient-basiclite-linuxx64.zip \
            && rm -f instantclient-basiclite-linuxx64.zip \
            && cd /opt/oracle/instantclient* \
            && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
            && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
            && ldconfig

WORKDIR    /app

ADD *.py .

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY .env .env

COPY rar_query.sql rar_query.sql 

RUN mkdir /extracts

CMD ["python3", "./oracle_db_extract.py"]