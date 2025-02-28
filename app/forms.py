from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Image', validators=
    [FileRequired(), FileAllowed(['jpg','png','jpeg'],
    'Only Images Allowed!')])
    
