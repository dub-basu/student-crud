from wtforms import Form, StringField, IntegerField, validators, SubmitField

class StudentForm(Form):
    """ Create a form class to get student information. """
    roll_number = IntegerField('ROLL NUMBER', [validators.required()])
    name = StringField('NAME', [validators.required()])
    rank = IntegerField('RANK')
