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


@team_members_blueprint.route('/team_members/managers')
def managers():
    return render_template('managers.html')


@team_members_blueprint.route('/team_members/data_scientists')
def data_scientists():
    return render_template('data_scientists.html')


@team_members_blueprint.route('/team_members/data_engineers')
def data_engineers():
    return render_template('data_engineers.html')


@team_members_blueprint.route('/team_members/qa_engineers')
def qa_engineers():
    return render_template('qa_engineers.html')


@team_members_blueprint.route('/team_members/devops_engineers')
def devops_engineers():
    return render_template('devops_engineers.html')


@team_members_blueprint.route('/team_members/project_management')
def project_management():
    return render_template('project_management.html')
