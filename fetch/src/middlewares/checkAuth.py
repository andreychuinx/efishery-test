from flask import request, abort, session, jsonify
from src.config.requestHandler import postRequest

def checkAuth():
    token = request.headers.get('Authorization')
    if not session.get('user'):
        response = postRequest('http://localhost:3000/api/check', headers= {
            'Authorization': f'{token}',
            'Content-Type': 'application/json'
        })
        if 'error' in response:
            return { 'error': 'Authencation failed'}
        else:
            session['user'] = response
            return { 'success': True }
    else:
        return { 'success': True}