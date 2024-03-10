""" Main file to run the application """
from flask import Flask
import src.infra.routes.user as user_routes

app = Flask(__name__)

app.register_blueprint(user_routes.bp)

if __name__ == '__main__':
    app.run()
