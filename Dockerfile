FROM        python:3.7-slim

RUN         apt -y update && apt -y dist-upgrade && apt -y autoremove
RUN         apt-get install -y procps
RUN         apt -y install vim
RUN         apt -y install nginx


COPY		./requirements.txt /tmp/
RUN			pip install -r /tmp/requirements.txt

COPY		. /srv/church_report
WORKDIR		/srv/church_report/app

RUN         rm /etc/nginx/sites-enabled/default
RUN         cp /srv/church_report/.config/local_dev/report.nginx /etc/nginx/sites-enabled/

RUN         mkdir   /var/log/gunicorn

CMD         /bin/bash
