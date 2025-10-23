from blacklists.src.errors.errors import ApiError
from blacklists.src.blueprints.blacklists import blacklists_blueprint
from blacklists.src.models.model import Base 
from blacklists.src.session import Session, engine
from flask import Flask, jsonify

application = Flask(__name__)
application.register_blueprint(blacklists_blueprint)

Base.metadata.create_all(engine)

@application.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "msg": err.description
    }
    return jsonify(response), err.code

if __name__ == "__main__":
    application.run(port = 5000, debug = True)
