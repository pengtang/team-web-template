from flask import Blueprint, render_template


home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


@home_blueprint.route('/')
def home():
    return render_template('index.html')


