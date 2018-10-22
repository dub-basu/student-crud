import sqlite3

from utils import Student

class DBHandler:

    def __init__(self, dbname):
        self.connection = sqlite3.connect(dbname)
        self.cursor  = self.connection.cursor()
        self.prepare_db()

    def prepare_db(self):
        with open('schema.sql', 'r') as f:
            cmd = f.read()
            self.cursor.execute(cmd)
            self.commit()

    def add_student(self, student):
        cmd = """INSERT INTO student VALUES ( {}, "{}" , {});""".format(
            student.roll_number,
            student.name,
            student.rank
        )
        self.cursor.execute(cmd)
        self.commit()

    def get_all_students(self):
        cmd = """SELECT * FROM student;"""
        students = [Student(*row) for row in self.cursor.execute(cmd)]
        return(students)

    def commit(self):
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
