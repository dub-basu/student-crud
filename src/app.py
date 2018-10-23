from flask import *

from forms import StudentForm
from utils import Student
from db import DBHandler

app = Flask(__name__)
DBNAME = 'db.sqlite3'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view')
def view_all():
    db = DBHandler(DBNAME)
    students = db.get_all_students()
    # TODO: merge_sort(student_list)
    return render_template('view_all.html', student_list = students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    form = StudentForm(request.form)
    
    if request.method == 'POST' and form.validate():
        
        student = Student(
            form.roll_number.data,
            form.name.data,
            form.rank.data
        )

        db = DBHandler(DBNAME)
        db.add_student(student)
        db.close_connection()

        return redirect(url_for('view_all'))

    elif request.method == 'GET':
        return render_template('add.html', form=form)
