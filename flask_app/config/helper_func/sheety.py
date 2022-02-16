import requests
from flask_app.models import model_student, model_cohort_student

def get_sheety(url):
    url = "https://api.sheety.co/e634878b511e89c78955e868629c69eb/sheetyInterface/attendance"
    headers = {
        'Authorization': 'Bearer 9d45b27c-e5c7-4daa-bcf5-ab110808b5a7'
    }
    resp = requests.request('GET', url, headers=headers)
    return resp.json()


def bulk_create_students(students, cohort_id):
    all_students = []
    for student in students:
        data = {
            'first_name': student['firstName'],
            'last_name': student['lastName'],
            'email': student['email'],
            'belt_score': student['beltScore'],
            'student_id': student['studentId'],
            'ap_status': student['apStatus'],
            'ap_count': student['apCount'],
            'sessions_present': student['p'],
            'sessions_late': student['l'],
            'sessions_excussed': student['e'],
            'sessions_absent': student['a'],
        }
        all_students.append(model_student.Student.create(**data))

    for student in all_students:
        model_cohort_student.CohortHasStudent.create(cohort_id=cohort_id, student_id=student.id)
    
    return True

