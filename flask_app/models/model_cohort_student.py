from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class CohortHasStudent(model_base.base_model):
    table = 'CohortHasStudents'
    def __init__(self, data):
        super().__init__(data)
        self.cohort_id = data['cohort_id']
        self.student_id = data['student_id']

