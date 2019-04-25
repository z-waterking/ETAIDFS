from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Required
from flask_wtf import FlaskForm

#登录表单
class Login_Form(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField('Login in')


#注册表单
class Register_Form(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    repassword = PasswordField('Repassword',validators=[DataRequired()])
    submit = SubmitField('Register')