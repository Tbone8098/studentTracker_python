from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class User(model_base.base_model):
    table = 'Users'
    def __init__(self, data):
        super().__init__(data)


    # Validator
    @staticmethod
    def validation(data):
        errors = {}

        if len(data['first_name']) < 1: 
            errors['User_first_name'] = 'first_nameis required'
        
        return errors
    
    # API Validator
    @staticmethod
    def validation(data):
        errors = {}

        if len(data['first_name']) < 1: 
            errors['User_first_name'] = 'first_name is required'
        
        return errors