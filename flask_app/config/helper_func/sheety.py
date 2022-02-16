import requests
from flask_app.models import model_student, model_cohort_student

def get_sheety(url):
    data = {}
    url = "https://api.sheety.co/e634878b511e89c78955e868629c69eb/sheetyInterface/attendance"
    headers = {
        'Authorization': 'Bearer 9d45b27c-e5c7-4daa-bcf5-ab110808b5a7'
    }
    resp = requests.request('GET', url, headers=headers)
    attendance = resp.json()
    data = {}
    for item in attendance:
        print(item)

    # url = "https://api.sheety.co/e634878b511e89c78955e868629c69eb/sheetyInterface/progress"
    # headers = {
    #     'Authorization': 'Bearer 9d45b27c-e5c7-4daa-bcf5-ab110808b5a7'
    # }
    # resp = requests.request('GET', url, headers=headers)
    # progress = resp.json()

    # data[attendance]
    # data[progress]
    # print(data)
    print(attendance)
    return attendance



def bulk_create_students(students, cohort_id):
    all_students = []
    for student in students['attendance']:
        if student['firstName']:
            data = {
                'first_name': student['firstName'],
                'last_name': student['lastName'],
                'email': student['email'],
                'belt_score': 0,
                'student_id': student['studentId'],
                'ap_status': student['apStatus'],
                'ap_count': {student['apCount'] if student['apCount'] != '' else 0},
                'sessions_present': {student['presentCount'] if student['presentCount'] != '' else 0},
                'sessions_late': {student['lateCount'] if student['lateCount'] != '' else 0},
                'sessions_excussed': {student['excusedCount'] if student['excusedCount'] != '' else 0},
                'sessions_absent': {student['absentCount'] if student['absentCount'] != '' else 0},
            }
            all_students.append(model_student.Student.create(**data))

    for id in all_students:
        model_cohort_student.CohortHasStudent.create(cohort_id=cohort_id, student_id=id)
    
    return True

