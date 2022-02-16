from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class CohortsHasUser(model_base.base_model):
    table = 'cohorts_has_users'
    def __init__(self, data):
        super().__init__(data)
        self.cohort_id = data['cohort_id']
        self.user_id = data['user_id']


    # Validator
    @staticmethod
    def validation(data):
        errors = {}

        if len(data['column name']) < 1: 
            errors['CohortsHasUser_column name'] = 'column nameis required'
        
        return errors
    
    # API Validator
    @staticmethod
    def validation(data):
        errors = {}

        if len(data['column name']) < 1: 
            errors['CohortsHasUser_column name'] = 'column name is required'
        
        return errors