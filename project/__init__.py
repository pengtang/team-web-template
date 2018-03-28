from flask import Flask, render_template

from project.home.views import home_blueprint
# from project.team_projects.views import team_projects_blueprint
from project.team_resources.views import team_resources_blueprint
from project.team_resources.onboarding.views import onboarding_blueprint
from project.team_members.views import team_members_blueprint
from project.users.views import users_blueprint
from project.blogs.views import blogs_blueprint

from project.extensions import bcrypt, csrf_protect, login_manager, db, migrate, cache, debug_toolbar
from project.config import ProdConfig


author = 'Peng Tang'
email = 'ptang@dstsystems.com'


def create_app(config_object=ProdConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    # register_shellcontext(app)
    # register_commands(app)
    # print(app.url_map)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    # webpack.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(home_blueprint)
    app.register_blueprint(team_resources_blueprint)
    app.register_blueprint(onboarding_blueprint)
    app.register_blueprint(team_members_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(blogs_blueprint)
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code), author=author, email=email), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


# def register_shellcontext(app):
#     """Register shell context objects."""
#     def shell_context():
#         """Shell context objects."""
#         return {
#             'db': db,
#             'User': users_blueprint}
#
#     app.shell_context_processor(shell_context)


# def register_commands(app):
#     """Register Click commands."""
#     app.cli.add_command(commands.test)
#     app.cli.add_command(commands.lint)
#     app.cli.add_command(commands.clean)
#     app.cli.add_command(commands.urls)


# app = Flask(__name__, static_url_path='/static')  # static_url_path is import in html image rendering
# app.secret_key = 'monkey'
# author = 'Peng Tang'
# email = 'ptang@dstsystems.com'
#
#
# bcrypt = Bcrypt(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# db = SQLAlchemy(app)
# app.config.from_object(os.environ['APP_SETTINGS'])
#
#
# # register our blueprints
# app.register_blueprint(home_blueprint)
# app.register_blueprint(team_resources_blueprint)
# app.register_blueprint(onboarding_blueprint)
# app.register_blueprint(team_members_blueprint)
# app.register_blueprint(users_blueprint)
#
#
# # Handle 404
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html', author=author, email=email)
#
