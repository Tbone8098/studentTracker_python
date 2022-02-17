from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_note, model_user, model_student

@app.route('/note/new')
@app.route('/note/new/<int:id>')
def new_note(id=0):
    session['page'] = 'New Note'
    context = {
        'user': model_user.User.get_one(id=session['uuid'])
    }
    if id > 0: 
        context['student'] = model_student.Student.get_one(id=id)
    else:
        context['all_students'] = model_student.Student.get_all()

    return render_template('main/note_new.html', **context)

@app.route('/note/create', methods=['post'])
def create_note():
    if not model_note.Note.validation(request.form):
        return redirect('/note/new')

    id = model_note.Note.create(**request.form)
    print(id)

    return redirect('/')

@app.route('/note/<int:id>')
def show_note(id):
    pass 

@app.route('/note/<int:id>/edit')
def edit_note(id):
    pass 

@app.route('/note/<int:id>/update', methods=['post'])
def update_note(id):

    if not model_note.Note.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    model_note.Note.update_one(id=id, **data)

    pass 

@app.route('/note/<int:id>/delete')
def delete_note(id):
    model_note.Note.delete_one(id=id)
    pass 


# ************************************************ API

# @app.route('/api/note/create', methods=['post'])
# def api_create_note():
#     errors = model_note.Note.validation(request.form)

#     if len(errors) > 0:
#         return jsonify(status=400, errors=errors)

#     data = {
#         **request.form
#     }

#     id = model_note.Note.create(**data)

#     return jsonify(status=200) 

# @app.route('/api/note/<int:id>')
# def api_show_note(id):

#     return jsonify(status=200) 

# @app.route('/api/note/<int:id>/edit')
# def api_edit_note(id):
    
#   return jsonify(status=200)  

# @app.route('/api/note/<int:id>/update', methods=['post'])
# def api_update_note(id):
#     errors = model_note.Note.validation(request.form)

#     if len(errors) > 0:
#         return jsonify(status=400, errors=errors)

#     data = {
#         **request.form
#     }

#     model_note.Note.update_one(id=id, **data)

#     return jsonify(status=200) 

# @app.route('/api/note/<int:id>/delete')
# def api_delete_note(id):
#     model_note.Note.delete_one(id=id)
#     return jsonify(status=200) 