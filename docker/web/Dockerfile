FROM python:3

WORKDIR /data/projects/portal_v3/docker/web

COPY requirements.txt .
COPY entrypoint.sh .

COPY apps .
COPY portal .
COPY templates .

RUN apt-get update && apt-get install vim cron libsasl2-dev python-dev libldap2-dev libssl-dev -y
RUN pip install -r requirements.txt && chmod +x /data/projects/portal_v3/docker/web/entrypoint.sh

RUN service cron start

ENTRYPOINT ["/data/projects/portal_v3/docker/web/entrypoint.sh"]