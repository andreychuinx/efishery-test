from flask import Flask, jsonify
from src.middlewares.checkAuth import checkAuth
from src.controllers.controller import getData, aggregate
from dotenv import load_dotenv

load_dotenv()

from flask_caching import Cache

app = Flask(__name__)
app.secret_key = 'TEST'
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/api/price', methods= ['GET'])
@cache.cached(timeout=600, unless=lambda: request.headers.get('If-Modified-Since'))
def price():
    check = checkAuth('all')
    if 'error' in check:
       return jsonify({'Error': 'Unauthorized'}), 401
    return getData()
# app.config["DEBUG"] = True
# Create some test data for our catalog in the form of a list of dictionaries.

@app.route('/api/aggregate', methods= ['GET'])
def getAggregateAuth():
    check = checkAuth('admin')
    if 'error' in check:
        return jsonify({'Error': 'Unauthorized'}), 401
    @cache.cached(timeout=600)
    def getAggregate():
        return aggregate()
    return getAggregate()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001)