from flask import Flask, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.views.auth import auth_app
from blog.models.database import db
from blog.models.auth import login_manager
import os
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SECRET_KEY"] = 'abcdefg123456'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/")
def index():
    return render_template("index.html")


app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")

cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.configs.{cfg_name}")
db.init_app(app)
login_manager.init_app(app)

migrate = Migrate(app, db)
migrate.init_app(app)
