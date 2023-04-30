from flask import jsonify
from src.config.requestHandler import getRequest
import os
import moment
from datetime import datetime
import statistics
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

def aggregate():
    response = getRequest('https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list')
    def changeData(acc, result):
        if (len(acc) == 0):
            return result
        else:
            newData = acc[0]
            if (newData['tgl_parsed'] is not None):
                dateParsed = moment.date(newData['tgl_parsed'])
                week = datetime(dateParsed.year, dateParsed.month, dateParsed.day).isocalendar().week
                newObj = {
                    'area_provinsi': newData['area_provinsi'],
                    'tahun': dateParsed.year,
                    'minggu': week,
                    'aggregate': {
                        'price': {},
                        'size': {}
                    }
                }
                findIndex = -1
                for i, item in enumerate(result):
                    count = 0
                    for k, v in item.items():
                        if v == newData['area_provinsi'] :
                            count +=1
                        if k == 'minggu':
                            if int(v) == int(week):
                                count+=1
                        if count == 2:
                            break
                    if count == 2:
                        findIndex = i
                        break
                if findIndex == -1:
                    newObj['aggregate']['price'] = {
                        "data": [int(newData['price'])],
                        "min": int(newData['price']),
                        "max": int(newData['price']),
                        "median": int(newData['price']),
                        "average": int(newData['price'])
                    }
                    newObj['aggregate']['size'] = {
                        "data": [int(newData['size'])],
                        "min": int(newData['size']),
                        "max": int(newData['size']),
                        "median": int(newData['size']),
                        "average": int(newData['size'])
                    }
                    result.append(newObj)
                else:
                    result[findIndex]['aggregate']['price']['data'].append(int(newData['price']))
                    result[findIndex]['aggregate']['price']['min'] = min(result[findIndex]['aggregate']['price']['data'])
                    result[findIndex]['aggregate']['price']['max'] = max(result[findIndex]['aggregate']['price']['data'])
                    result[findIndex]['aggregate']['price']['median'] =statistics.median(result[findIndex]['aggregate']['price']['data'])
                    result[findIndex]['aggregate']['price']['average'] =statistics.mean(result[findIndex]['aggregate']['price']['data'])

                    result[findIndex]['aggregate']['size']['data'].append(int(newData['size']))
                    result[findIndex]['aggregate']['size']['min'] = min(result[findIndex]['aggregate']['size']['data'])
                    result[findIndex]['aggregate']['size']['max'] = max(result[findIndex]['aggregate']['size']['data'])
                    result[findIndex]['aggregate']['size']['median'] =statistics.median(result[findIndex]['aggregate']['size']['data'])
                    result[findIndex]['aggregate']['size']['average'] =statistics.mean(result[findIndex]['aggregate']['size']['data'])
            return changeData(acc[1:], result)
    return jsonify(changeData(response, []))