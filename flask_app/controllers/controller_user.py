from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_user

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')

@app.route('/user/login', methods=['post'])
def new_user():
    if not model_user.User.validation_login(request.form):
        return redirect('/') 

    data = {
        **request.form
    }

    id = model_user.User.create(**data)

    return redirect('/')

@app.route('/user/register')
def register():

    return render_template('landing_page/register.html')

@app.route('/user/create', methods=['post'])
def create_user():

    if not model_user.User.validation(request.form):
        return redirect('/user/register')

    hash_pw = bcrypt.generate_password_hash(request.form['pw'])

    data = {
        **request.form,
        'pw': hash_pw
    }

    del data['confirm_pw']

    print(data)

    id = model_user.User.create(**data)
    session['uuid'] = id

    return redirect('/') 

@app.route('/user/<int:id>')
def show_user(id):
    pass 

@app.route('/user/<int:id>/edit')
def edit_user(id):
    pass 

@app.route('/user/<int:id>/update', methods=['post'])
def update_user(id):

    if not model_user.User.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    model_user.User.update_one(id=id, **data)

    pass 

@app.route('/user/<int:id>/delete')
def delete_user(id):
    model_user.User.delete_one(id=id)
    pass 


# ************************************************ API

# @app.route('/api/user/create', methods=['post'])
# def api_create_user():
#     errors = model_user.User.validation(request.form)

#     if len(errors) > 0:
#         return jsonify(status=400, errors=errors)

#     data = {
#         **request.form
#     }

#     id = model_user.User.create(**data)

#     return jsonify(status=200) 

# @app.route('/api/user/<int:id>')
# def api_show_user(id):

#     return jsonify(status=200) 

# @app.route('/api/user/<int:id>/edit')
# def api_edit_user(id):
    
#   return jsonify(status=200)  

# @app.route('/api/user/<int:id>/update', methods=['post'])
# def api_update_user(id):
#     errors = model_user.User.validation(request.form)

#     if len(errors) > 0:
#         return jsonify(status=400, errors=errors)

#     data = {
#         **request.form
#     }

#     model_user.User.update_one(id=id, **data)

#     return jsonify(status=200) 

# @app.route('/api/user/<int:id>/delete')
# def api_delete_user(id):
#     model_user.User.delete_one(id=id)
#     return jsonify(status=200) 