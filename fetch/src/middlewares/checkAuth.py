from flask import request, abort, session, jsonify
from src.config.requestHandler import postRequest
from datetime import datetime
def checkAuth(role):
    token = request.headers.get('Authorization')
    response = postRequest('http://localhost:3000/api/check', headers= {
            'Authorization': f'{token}',
            'Content-Type': 'application/json',
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            'Cache-Control': 'public, max-age=0',
            'Last-Modified': datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        })
    if 'error' in response:
        return { 'error': 'Authencation failed'}
    if role != 'all':
        if role != str(response['role']):
            return { 'error': 'Authorization failed'}
    return { 'success': True}