from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email


class UserForm(FlaskForm):
    name = StringField(label="Name", name="user-name", validators=[DataRequired()])
    username = StringField(
        label="Username",
        name="user-username",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
    )
    email = StringField(label="Email", name="user-email", validators=[Email()])
