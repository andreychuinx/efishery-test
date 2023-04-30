from flask import jsonify
from src.config.requestHandler import getRequest
import os

def getData():
    response = getRequest('https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list')
    apiKey = os.getenv('API_KEY_CONVERTER')
    currencyConverter = getRequest(f'https://api.freecurrencyapi.com/v1/latest?apikey={apiKey}')
    idrRate = currencyConverter['data']['IDR']
    newResponse = list(map(lambda data: {
        "area_kota": data['area_kota'],
		"area_provinsi": data['area_provinsi'],
		"komoditas": data['komoditas'],
		"price": data['price'],
		"size": data['size'],
		"tgl_parsed": data['tgl_parsed'],
		"timestamp": data['timestamp'],
		"uuid": data['uuid'],
        "price_usd": None if data['price'] == None else int(data['price']) / idrRate
    }, response))
    return jsonify(newResponse)