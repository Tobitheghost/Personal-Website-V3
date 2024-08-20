from flask import render_template, redirect, Blueprint, request, flash, url_for, after_this_request, session
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFError
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import logging
from .email import check_email
from . import path_links

logger = logging.getLogger()
home = Blueprint('home',__name__,url_prefix="/")

class Contact_Me(FlaskForm):
    name = StringField('Your Name*', validators=[DataRequired()])
    email = EmailField('Your Email*', validators=[DataRequired(), Email()])
    textarea = TextAreaField('Your Message', validators=[DataRequired()])
    submitbtn = SubmitField('Send Message')
    test = StringField('1 + 5', validators=[DataRequired()])
    
@home.before_request
def send_session():
    
    session_log = {"Session Log" : [{"forwarded_for": request.headers.get("X_FORWARDED_FOR")}, 
        {"real_ip": request.headers.get("X_REAL_IP")}, 
        {"host": request.headers.get("HOST")},
        {"request": request.url},
        {"user_agent": str(request.user_agent)},
        {"proxy_ip": request.remote_addr}]}
    
    if request.headers.get("X_REAL_IP") in session:
        if session["log"]:
            session["log"].append(session_log)
        else:
            session["log"] = [session_log]
    else:
        session["ip"] = request.headers.get("X_REAL_IP")
        session["log"] = (session_log)
        
    logger.debug(session)


@home.route('/', methods=('GET', 'POST'))
def landing():
    form = Contact_Me()
    response = None
    if request.method == "POST":
        if form.validate_on_submit():
            response = check_email(form.name.data, form.textarea.data, form.email.data, form.test.data)
            resonse_log = {
            "response": response,
            "name": form.name.data,
            "email_msg": form.textarea.data,
            "email": form.email.data,}
            logger.debug(resonse_log)
        else:
            response = "There seems to be an error with your connection" ,"error"
            resonse_log = {
            "response": response,
            "name": form.name.data,
            "email_msg": form.textarea.data,
            "email": form.email.data,}
            logger.error(resonse_log)
        session["name"] = form.name.data
        session["email"] = form.email.data
        flash(response)
        print(response)
        return render_template("recruiter_landing.html", form=form, response=response)
    return render_template("recruiter_landing.html", form=form, response=response)

@home.route('/test', methods=('GET', 'POST'))
def test():
    return render_template("menu_grid.html", path_links=path_links)

#Errors
@home.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('errors\csrf_error.html', reason=e.description, handler=True), 400
