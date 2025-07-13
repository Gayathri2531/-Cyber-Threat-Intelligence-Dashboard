import os, requests
API_KEY = os.getenv("VT_API_KEY")
def lookup_url_ip(ip=None, domain=None):
    url = domain or ip
    endpoint = 'ip-address' if ip else 'domain'
    resp = requests.get('https://www.virustotal.com/vtapi/v2/'+endpoint+'/report',
        params={'apikey': API_KEY, endpoint: url})
    return resp.json()