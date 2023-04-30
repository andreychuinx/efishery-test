import requests
from requests.exceptions import HTTPError

def getRequest(url: str):
  res = requests.get(url)
  if res.status_code == 200:
    return res.json()
  else:
     return  { 'code': res.status_code, 'error': res.json() }

def postRequest(url: str, headers):
  res = requests.post(url, headers=headers)
  if res.status_code == 200:
      return res.json()
  else:
      return { 'code': res.status_code, 'error': res.json() }