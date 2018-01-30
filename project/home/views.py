import os
from flask import render_template, Blueprint, send_from_directory
# from flask.ext.login import login_required, current_user


home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


# @home_blueprint.route('/upload/<filename>')
# def send_image(filename):
#     return send_from_directory('images', filename)


# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])
# @login_required
def home():
    # base_path = os.path.dirname(os.path.abspath(__file__))
    # images = os.listdir('project/home/images')
    # print(images)
    return render_template('index.html')
