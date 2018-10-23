from flask import *

from utils import Student
from db import DBHandler

app = Flask(__name__)
DBNAME = 'db.sqlite3'

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/view')
def view_all():
    db = DBHandler(DBNAME)
    students = db.get_all_students()
    # TODO: merge_sort(student_list)
    return render_template('view_all.html', student_list = students)
