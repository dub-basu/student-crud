from wtforms import Form, StringField, IntegerField, validators, SubmitField

class StudentForm(Form):
    """ Create a form class to get student information. """
    roll_number = IntegerField('Roll Number', [validators.required()])
    name = StringField('Name', [validators.required()])
    rank = IntegerField('Rank')
