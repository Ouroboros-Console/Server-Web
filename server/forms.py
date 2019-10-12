from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from server.models import User


class RegistrationForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired(), Email()])

    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=4, max=15)]
    )

    confirm_password = PasswordField(
        "Re-type Password", validators=[DataRequired(), EqualTo("password")]
    )

    address = TextAreaField(
        "Your Address", validators=[DataRequired(), Length(min=10, max=200)]
    )

    submit = SubmitField("SIGN UP")

    # Custom validator for existing email
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError("That email is taken! Please choose  a different one")
