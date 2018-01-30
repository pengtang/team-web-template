from flask import render_template, Blueprint


onboarding_blueprint = Blueprint(
    'onboarding', __name__,
    template_folder='templates'
)


@onboarding_blueprint.route('/team_resources/onboarding', methods=['GET', 'POST'])
def onboarding():
    return render_template('onboarding.html')
