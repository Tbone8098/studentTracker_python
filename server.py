from flask_app import app
from flask_app.controllers import controller_routes, controller_user, controller_cohort, controller_student, controller_note

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')