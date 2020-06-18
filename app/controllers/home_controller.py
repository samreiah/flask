from flask import request, jsonify, render_template, session
from datetime import datetime

def index():
    isLoggedIn = False
    if 'customerid' in session:
        isLoggedIn = True
        customerName = session['name']
    return render_template('home/index.html', now = datetime.utcnow(), isLoggedIn = isLoggedIn, customerName = customerName)