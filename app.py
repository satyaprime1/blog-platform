from flask import Flask, render_template

from config import Config
from extensions import db, login_manager

from models.user import User
from models.post import Post
from models.comment import Comment

from routes.auth_routes import auth
from routes.post_routes import post
from routes.comment_routes import comment
from routes.api_routes import api


app = Flask(__name__)

app.config.from_object(Config)


# Initialize extensions
db.init_app(app)
login_manager.init_app(app)


# Login configuration
login_manager.login_view = "auth.login"


# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(post)
app.register_blueprint(comment)
app.register_blueprint(api)


@login_manager.user_loader
def load_user(user_id):

    return db.session.get(
        User,
        int(user_id)
    )


@app.route("/")
def home():

    return render_template(
        "home.html"
    )


if __name__ == "__main__":

    with app.app_context():

        db.create_all()

    print("Starting Flask...")

    app.run(
        debug=True
    )