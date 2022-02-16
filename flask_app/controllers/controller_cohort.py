from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_cohort, model_cohorts_has_users, model_user
from flask_app.config.helper_func.sheety import get_sheety, bulk_create_students

@app.route('/cohort/new')
def new_cohort():
    session['page'] = 'cohort_new'
    context = {
        'user': model_user.User.get_one(id=session['uuid'])
    }
    return render_template('/main/cohort_new.html', **context)

@app.route('/cohort/create', methods=['post'])
def create_cohort():

    if not model_cohort.Cohort.validation(request.form):
        return redirect('/')

    data = {
        **request.form,
        'user_id': session['uuid']
    }

    id = model_cohort.Cohort.create(**data)

    students = get_sheety(request.form['sheetyInterface'])
    print(students)

    bulk_create_students(students, id)

    model_cohorts_has_users.CohortsHasUser.create(cohort_id=id, user_id=session['uuid'])

    return redirect('/')

@app.route('/cohort/<int:id>')
def show_cohort(id):
    session['page'] = 'cohort_show'
    context = {
        'user': model_user.User.get_one(id=session['uuid']),
        'cohort': model_cohort.Cohort.get_one(id=id)
    }
    return render_template('/main/cohort_show.html', **context)

@app.route('/cohort/<int:id>/edit')
def edit_cohort(id):
    pass 

@app.route('/cohort/<int:id>/update', methods=['post'])
def update_cohort(id):

    if not model_cohort.Cohort.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    model_cohort.Cohort.update_one(id=id, **data)

    pass 

@app.route('/cohort/<int:id>/delete')
def delete_cohort(id):
    model_cohort.Cohort.delete_one(id=id)
    pass 


# ************************************************ API

# @app.route('/api/cohort/create', methods=['post'])
# def api_create_cohort():
#     errors = model_cohort.Cohort.validation(request.form)

#     if len(errors) > 0:
#         return jsonify(status=400, errors=errors)

#     data = {
#         **request.form
#     }

#     id = model_cohort.Cohort.create(**data)

#     return jsonify(status=200) 

# @app.route('/api/cohort/<int:id>')
# def api_show_cohort(id):

#     return jsonify(status=200) 

# @app.route('/api/cohort/<int:id>/edit')
# def api_edit_cohort(id):
    
#   return jsonify(status=200)  

# @app.route('/api/cohort/<int:id>/update', methods=['post'])
# def api_update_cohort(id):
#     errors = model_cohort.Cohort.validation(request.form)

#     if len(errors) > 0:
#         return jsonify(status=400, errors=errors)

#     data = {
#         **request.form
#     }

#     model_cohort.Cohort.update_one(id=id, **data)

#     return jsonify(status=200) 

# @app.route('/api/cohort/<int:id>/delete')
# def api_delete_cohort(id):
#     model_cohort.Cohort.delete_one(id=id)
#     return jsonify(status=200) 