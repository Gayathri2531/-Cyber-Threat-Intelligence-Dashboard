import os, requests
API_KEY = os.getenv("ABUSEIPDB_KEY")
def check_ip(ip):
    resp = requests.get('https://api.abuseipdb.com/api/v2/check',
        params={'ipAddress': ip},
        headers={'Key': API_KEY, 'Accept': 'application/json'})
    return resp.json()