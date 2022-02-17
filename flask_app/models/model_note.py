from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class Note(model_base.base_model):
    table = 'notes'
    def __init__(self, data):
        super().__init__(data)
        self.content = data['content']
        self.student_id = data['student_id']


    # Validator
    @staticmethod
    def validation(data):
        is_valid = True
        print(data)

        if len(data['content']) < 1: 
            print('false 1' )
            flash('content of the message must hold some content', 'err_note_content')
            is_valid = False        

        if not int(data['student_id']) > 0: 
            print('false 2' )
            flash('Must pick a student', 'err_note_student_id')
            is_valid = False

        print(is_valid)
        
        return is_valid
    
    # # API Validator
    # @staticmethod
    # def validation(data):
    #     errors = {}

    #     if len(data['column name']) < 1: 
    #         errors['Noe_column name'] = 'column name is required'
        
    #     return errors