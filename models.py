from flask_pymongo import PyMongo
mongo = PyMongo()
def init_db(app):
    app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost/ctidb")
    mongo.init_app(app)

class IOC:
    def __init__(self, ip, vt, abuse, tags):
        self.data = {'ip': ip, 'vt': vt, 'abuse': abuse, 'tags': tags}
    def save(self):
        mongo.db.iocs.insert_one(self.data)