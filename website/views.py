from flask import render_template, redirect, Blueprint, request, flash, url_for, after_this_request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFError
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from .email import check_email

home = Blueprint('home',__name__,url_prefix="/")

class Contact_Me(FlaskForm):
    name = StringField('Your Name*', validators=[DataRequired()])
    email = EmailField('Your Email*', validators=[DataRequired(), Email()])
    textarea = TextAreaField('Your Message', validators=[DataRequired()])
    submitbtn = SubmitField('Send Message')
    test = StringField('1 + 5', validators=[DataRequired()])

@home.route('/', methods=('GET', 'POST'))
def landing():
    form = Contact_Me()
    response = None
    if request.method == "POST":
        if form.validate_on_submit():
            response = check_email(form.name.data, form.textarea.data, form.email.data, form.test.data)
        else:
            response = "There seems to be an error with your connection" ,"error"
        flash(response)
        print(response)
        return render_template("recruiter_landing.html", form=form, response=response)
    
    return render_template("recruiter_landing.html", form=form, response=response)

#Errors
@home.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description, handler=True), 400