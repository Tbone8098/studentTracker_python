from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class Student(model_base.base_model):
    table = 'students'
    def __init__(self, data):
        super().__init__(data)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.belt_score = data['belt_score']
        self.student_id = data['student_id']
        self.ap_status = data['ap_status']
        self.ap_count = data['ap_count']
        self.sessions_present = data['sessions_present']
        self.sessions_late = data['sessions_late']
        self.sessions_excussed = data['sessions_excussed']
        self.sessions_absent = data['sessions_absent']


    # Validator
    @staticmethod
    def validation(data):
        errors = {}

        if len(data['first_name']) < 1: 
            errors['Student_first_name'] = 'first_nameis required'
        
        return errors
    
    # API Validator
    @staticmethod
    def validation(data):
        errors = {}

        if len(data['first_name']) < 1: 
            errors['Student_first_name'] = 'first_name is required'
        
        return errors