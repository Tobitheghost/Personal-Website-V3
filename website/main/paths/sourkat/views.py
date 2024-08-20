from flask import render_template, Blueprint, request, session
import logging

logger = logging.getLogger('views')
sourkat = Blueprint('sourkat',__name__,url_prefix="sourkat/")
    
@sourkat.before_request
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

@sourkat.route('/', methods=('GET', 'POST'))
def landing():
    return render_template('index.html')
