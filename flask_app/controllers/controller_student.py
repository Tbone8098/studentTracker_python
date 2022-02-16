from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_student

@app.route('/students/all')
def all_students():
    context = {
        'all_students': model_student.Student.get_all()
    }
    return render_template('/main/students_all.html', **context)

@app.route('/student/new')
def new_student():
    pass 

@app.route('/student/create', methods=['post'])
def create_student():

    if not model_student.Student.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    id = model_student.Student.create(**data)

    pass 

@app.route('/student/<int:id>')
def show_student(id):
    pass 

@app.route('/student/<int:id>/edit')
def edit_student(id):
    pass 

@app.route('/student/<int:id>/update', methods=['post'])
def update_student(id):

    if not model_student.Student.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    model_student.Student.update_one(id=id, **data)

    pass 

@app.route('/student/<int:id>/delete')
def delete_student(id):
    model_student.Student.delete_one(id=id)
    pass 


# ************************************************ API

# @app.route('/api/student/create', methods=['post'])
# def api_create_student():
#     errors = model_student.Student.validation(request.form)

#     if len(errors) > 0:
#         return jsonify(status=400, errors=errors)

#     data = {
#         **request.form
#     }

#     id = model_student.Student.create(**data)

#     return jsonify(status=200) 

# @app.route('/api/student/<int:id>')
# def api_show_student(id):

#     return jsonify(status=200) 

# @app.route('/api/student/<int:id>/edit')
# def api_edit_student(id):
    
#   return jsonify(status=200)  

# @app.route('/api/student/<int:id>/update', methods=['post'])
# def api_update_student(id):
#     errors = model_student.Student.validation(request.form)

#     if len(errors) > 0:
#         return jsonify(status=400, errors=errors)

#     data = {
#         **request.form
#     }

#     model_student.Student.update_one(id=id, **data)

#     return jsonify(status=200) 

# @app.route('/api/student/<int:id>/delete')
# def api_delete_student(id):
#     model_student.Student.delete_one(id=id)
#     return jsonify(status=200) 