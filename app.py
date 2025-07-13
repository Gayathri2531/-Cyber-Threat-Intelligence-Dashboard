from flask import Flask, render_template, request, jsonify
from virus_total import lookup_url_ip
from abuseipdb import check_ip
from models import init_db, IOC
app = Flask(__name__)
init_db(app)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    data = request.json
    ip = data.get('ip')
    vt = lookup_url_ip(ip=ip)
    ab = check_ip(ip)
    ioc = IOC(ip=ip, vt=vt, abuse=ab, tags=[])
    ioc.save()
    return jsonify({'vt': vt, 'abuse': ab})