from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_student
from flask_app import DATABASE_SCHEMA
import re

class Cohort(model_base.base_model):
    table = 'cohorts'
    def __init__(self, data):
        super().__init__(data)
        self.start_date = data['start_date']
        self.is_archived = data['is_archived']
        self.user_id = data['user_id']
        self.sheetyInterface = data['sheetyInterface']

    @property
    def students(self):
        # TODO make this a join statement in order to reduce database calls
        query = f"SELECT * FROM cohorts_has_students WHERE cohort_id={self.id};"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        if results:
            list_of_students = []
            for record in results:
                student = model_student.Student.get_one(id=record['student_id'])
                list_of_students.append(student)
            return list_of_students
        return []

    # Validator
    @staticmethod
    def validation(data):
        is_valid = True

        if len(data['start_date']) < 1: 
            flash('start_date is required', 'err_cohort_start_date')

        if len(data['sheetyInterface']) < 1: 
            flash('sheetyInterface is required', 'err_cohort_sheetyInterface')
        
        return is_valid