from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, InputRequired

class ContactForm(FlaskForm):
    username = StringField('Please enter your full name', validators=[InputRequired()])
    email = StringField('Please enter your e-mail address', validators = [InputRequired(), Email()])
    subject = StringField('Please enter the subject for the message', validators=[InputRequired()])
    message = TextAreaField('Please enter the message you would like to send', validators=[InputRequired()])
