import requests

# this example is meant for a basic health check program
# that sends mail if the url is unreachable
r = requests.get('10.0.0.61:3001/healthcheck')
if not r.status_code == 200:
    mail.send('fgh@.com')