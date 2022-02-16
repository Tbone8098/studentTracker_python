from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class Cohort(model_base.base_model):
    table = 'cohorts'
    def __init__(self, data):
        super().__init__(data)
        self.month = data['month']
        self.year = data['year']
        self.is_archived = data['is_archived']
        self.user_id = data['user_id']
        self.sheetyInterface = data['sheetyInterface']


    # Validator
    @staticmethod
    def validation(data):
        is_valid = True
        print(data)

        if len(data['start_date']) < 1: 
            flash('start_date is required', 'err_cohort_start_date')

        if len(data['sheetyInterface']) < 1: 
            flash('sheetyInterface is required', 'err_cohort_sheetyInterface')
        
        return is_valid