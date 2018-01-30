from flask import Flask, render_template
from flask import jsonify
# from flask.ext.bcrypt import Bcrypt
# from flask.ext.login import LoginManager
# from models import User
from project.home.views import home_blueprint
# from project.team_members.views import team_members_blueprint
# from project.team_projects.views import team_projects_blueprint
from project.team_resources.views import team_resources_blueprint
from project.team_resources.onboarding.views import onboarding_blueprint
from project.team_members.views import team_members_blueprint


app = Flask(__name__, static_url_path='/static')  # static_url_path is import in html image rendering
app.secret_key = 'monkey'
author = 'Peng Tang'
email = 'ptang@dstsystems.com'

# bcrypt = Bcrypt(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# app.config.from_object(os.environ['APP_SETTINGS'])
# db = SQLAlchemy(app)

# register our blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(team_resources_blueprint)
app.register_blueprint(onboarding_blueprint)
app.register_blueprint(team_members_blueprint)


# Handle 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', author=author, email=email)
