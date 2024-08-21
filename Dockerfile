FROM ubuntu:22.04

WORKDIR /work

EXPOSE 8000

ADD good-first-issue /work/
ADD requirements.txt /work/
RUN chmod +x /work/


RUN apt-get update -y && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

CMD ["gunicorn", "--config", "gunicorn_config.py", "app:app", "nginx"]