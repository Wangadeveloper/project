from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,TextAreaField,IntegerField,SelectField,FileField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6)]
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class UserProfileForm(FlaskForm):
    full_names = StringField("Full Names", validators=[DataRequired()])
    monthly_income = IntegerField("Monthly Income", validators=[DataRequired()])
    business_type = StringField("Business Type", validators=[DataRequired()])
    business_level = StringField("Business Level", validators=[DataRequired()])
    phone = StringField("Phone", validators=[DataRequired()])
    country = StringField("Country", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    submit = SubmitField("Save Profile")
    
class LoanRiskAssessmentForm(FlaskForm):
    loan_amount = IntegerField('Loan Amount', validators=[DataRequired()])
    monthly_income = IntegerField('Monthly Income', validators=[DataRequired()])
    
    business_type = SelectField('Business Type', 
                                choices=[('Sole Proprietorship', 'Sole Proprietorship'),
                                         ('Partnership', 'Partnership'),
                                         ('Corporation', 'Corporation')],
                                validators=[DataRequired()])
    
    business_level = SelectField('Business Level', 
                                 choices=[('Startup', 'Startup'),
                                          ('Growing', 'Growing'),
                                          ('Established', 'Established')],
                                 validators=[DataRequired()])
    
    repayment_period = IntegerField('Repayment Period (in months)', validators=[DataRequired()])
    
    business_desc = TextAreaField('Business Description', validators=[DataRequired()])
    
    # 👇 New language selection field
    language = SelectField('Preferred Language', 
                           choices=[('English', 'English'), ('Swahili', 'Swahili')], 
                           validators=[DataRequired()],
                           default='English')
    
    submit = SubmitField('Submit Assessment')
