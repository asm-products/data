FROM python:2.7
WORKDIR /tmp
ADD requirements.txt ./
RUN pip install --src /pylibs -r requirements.txt
RUN openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 -subj "/C=US/ST=State/L=City/O=Section/CN=domainname" -keyout site.key -out site.crt
