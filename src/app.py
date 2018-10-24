import sqlite3
from flask import *

from forms import StudentForm
from utils import Student, merge_sort
from db import DBHandler

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
DBNAME = 'db.sqlite3'

@app.route('/')
def home():
    """ View home page. """
    return render_template('home.html')

@app.route('/view')
def view_all():
    """ View list of students. """
    db = DBHandler(DBNAME)
    students = db.get_all_students()
    db.close_connection()
    students = merge_sort(students)
    return render_template('view_all.html', student_list = students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    """ View add student form. """
    form = StudentForm(request.form)

    if request.method == 'POST' and form.validate():
        
        student = Student(
            form.roll_number.data,
            form.name.data,
            form.rank.data
        )

        try:
            # Try to add student record to database
            db = DBHandler(DBNAME)
            db.add_student(student)
            db.close_connection()
        except sqlite3.IntegrityError as e:
            # Primary key constraint: Roll number already exists
            flash('Roll number already exists.')
            return render_template('add.html', form=form)
        
        return redirect(url_for('view_all'))

    return render_template('add.html', form=form)
    