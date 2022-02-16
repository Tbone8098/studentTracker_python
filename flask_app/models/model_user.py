from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import model_base, model_cohort
from flask_app import DATABASE_SCHEMA, bcrypt
import re

class User(model_base.base_model):
    table = 'Users'
    def __init__(self, data):
        super().__init__(data)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw = data['pw']

    @property
    def current_cohort(self):
        query = f"SELECT * FROM cohorts_has_users JOIN cohorts ON cohorts_has_users.cohort_id = cohorts.id WHERE cohorts_has_users.user_id = {self.id} ORDER BY cohort_id DESC LIMIT 1;"
        result = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        if result:
            data = {
                'id': result[0]['cohorts.id'],
                'created_at': result[0]['cohorts.created_at'],
                'updated_at': result[0]['cohorts.updated_at'],
                'start_date': result[0]['start_date'],
                'is_archived': result[0]['is_archived'],
                'user_id': result[0]['user_id'],
                'sheetyInterface': result[0]['sheetyInterface'],
                
            }
            return model_cohort.Cohort(data)
        return []


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

        else:
            potential_user = User.get_one(email=data['email'])
            if not potential_user:
                flash("Invalid Credentials", 'err_user_pw')
                is_valid = False
            elif not bcrypt.check_password_hash(potential_user.pw, data['pw']):
                flash("Invalid Credentials", 'err_user_pw')
                is_valid = False
            else:
                session['uuid'] = potential_user.id
        
        return is_valid
