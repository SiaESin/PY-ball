from flask import Blueprint, render_template, request, redirect


bp = Blueprint('animals', __name__, url_prefix="/animals")

@bp.route('/')
def index(): 
    return ('Index page' )

@bp.route('/show')
def show(id): 
    return render_template('animals/show.html')
