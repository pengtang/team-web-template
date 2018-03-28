from flask import render_template, Blueprint
from flask_login import login_required


team_resources_blueprint = Blueprint(
    'team_resources', __name__,
    template_folder='templates'
)


# use decorators to link the function to a url
@team_resources_blueprint.route('/team_resources', methods=['GET', 'POST'])
@login_required
def team_resources():
    return render_template('team_resources.html')
