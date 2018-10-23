from wtforms import Form, StringField, IntegerField, validators, SubmitField

class StudentForm(Form):
    roll_number = IntegerField('Roll Number', [validators.required()])
    name = StringField('Name', [validators.required()])
    rank = IntegerField('Rank')
