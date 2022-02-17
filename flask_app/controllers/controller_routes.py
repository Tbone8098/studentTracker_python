from email import header
from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_user
from flask_app.config.helper_func.sheety import get_sheety 

@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    session['page'] = 'landing_page'
    return render_template('landing_page/index.html')

@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    session['page'] = 'dashboard'    

    context = {
        'user': model_user.User.get_one(id=session['uuid'])
    }

    return render_template('main/dashboard.html', **context)

@app.route("/get_sheety")
def sheety():
    info = get_sheety(url='https://api.sheety.co/e634878b511e89c78955e868629c69eb/sheetyInterface/attendance')
    print(info)
    return redirect('/')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'page not found'