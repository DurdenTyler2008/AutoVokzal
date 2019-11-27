

FROM python:3.7
COPY src /opt/application/
COPY requirements.pip /tmp/requirements.pip
RUN pip install -r /tmp/requirements.pip

WORKDIR /opt/application

#CMD pytest