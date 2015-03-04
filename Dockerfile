FROM python:2.7
WORKDIR /tmp
ADD requirements.txt ./
RUN pip install --src /pylibs -r requirements.txt
