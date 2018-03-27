from project import create_app, db
from project.config import ProdConfig


app = create_app(config_object=ProdConfig)
with app.app_context():
    db.create_all()
