import werkzeug
from flask import render_template

#Errors

def unsupported_media_type(e):
    return render_template('errors\\unsupported_media_type_error.html', reason=e.description, handler=True, code=415), 415

def imateapot_error(e):
    return render_template('errors\\im_a_teapot_error.html', reason=e.description, handler=True, code=418), 418

class YouGotHigh(werkzeug.exceptions.HTTPException):
    code = 420
    description = 'You are trying to submit a request while high'

def weed_error(e):
    return render_template('errors\\weed_420_error.html', reason=e.description, handler=True, code=420), 420

def unavailable_for_legal_reasons(e):
    return render_template('errors\\unavailable_for_legal_reasons_error.html', reason=e.description, handler=True, code=451), 451

def infinite_loop_error(e):
    return render_template('errors\\infinite_loop_error.html', reason=e.description, handler=True, code=508), 508

def page_not_found(e):
    return render_template('errors\\error.html', reason=e.description, handler=True, code=404), 404

