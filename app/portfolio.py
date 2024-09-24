from flask import (
    Blueprint,render_template, request, redirect, url_for, current_app
)

bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html') 

@bp.route('/mail', methods=['POST'])
def mail():
    name = request.form 
    return render_template('portfolio/sent_mail.html')
    
