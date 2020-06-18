from flask import request, jsonify, render_template, flash, url_for, session, redirect
from flask_sqlalchemy import get_debug_queries
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from app.models.user import User

from app.forms.auth.login import LoginForm

def getLogin():
    if LoginForm().validate_on_submit():
        # Retrieve user with customer Id
        user = User.query.filter_by(customerid=request.form.get('customerId')).first()
        if(user):
            if check_password_hash(user.password, request.form.get('password')):
                session['isLoggedIn'] = True
                session['customerid'] = user.customerid
                session['id'] = user.id
                session['name'] = user.name
                flash("Successfully Logged In")
                return redirect('/')
            else:
                flash("Invalid Password")
                return redirect('/login')
        else:
            flash("Invalid Customer Id")
            return redirect('/login')
    else:
        return render_template('auth/login.html', now = datetime.utcnow(), form = LoginForm())

