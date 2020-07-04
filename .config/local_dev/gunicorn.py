daemon = False
chdir = '/srv/church_report/app'
bind = 'unix:/run/report.sock'
accesslog = '/var/log/gunicorn/report-access.log'
errorlog = '/var/log/gunicorn/report-error.log'
capture_output = True