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
        is_valid = True

        if len(data['first_name']) < 1: 
            flash('first_name is required', 'err_user_first_name')
            is_valid = False

        if len(data['last_name']) < 1: 
            flash('last_name is required', 'err_user_last_name')
            is_valid = False

        if len(data['email']) < 1: 
            flash('email is required', 'err_user_email')
            is_valid = False

        if len(data['pw']) < 1: 
            flash('password is required', 'err_user_pw')
            is_valid = False

        if len(data['confirm_pw']) < 1: 
            flash('confirm_password is required', 'err_user_confirm_pw')
            is_valid = False
        
        return is_valid
        
    # Validator
    @staticmethod
    def validation_login(data):
        is_valid = True

        if len(data['email']) < 1: 
            flash('email is required', 'err_user_email')
            is_valid = False

        if len(data['pw']) < 1: 
            flash('password is required', 'err_user_pw')
            is_valid = False
        
        return is_valid
