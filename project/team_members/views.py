from flask import render_template, Blueprint
# from flask.ext.login import login_required, current_user

team_members_blueprint = Blueprint(
    'team_members', __name__,
    template_folder='templates'
)


# use decorators to link the function to a url
@team_members_blueprint.route('/team_members', methods=['GET', 'POST'])
# @login_required
def team_members():
    return render_template('team_members.html')


@team_members_blueprint.route('/team_members/Maryssa_Metheny', methods=['GET', 'POST'])
# @login_required
def maryssa():
    return render_template('Maryssa_Metheny.html')


@team_members_blueprint.route('/team_members/Sangita_Sahoo', methods=['GET', 'POST'])
# @login_required
def sangita():
    return render_template('Sangita_Sahoo.html')
