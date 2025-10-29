from flask import Flask, jsonify

from blacklists.src.blueprints.blacklists import blacklists_blueprint
from blacklists.src.errors.errors import ApiError
from blacklists.src.models.model import Base
from blacklists.src.session import Session, engine

application = Flask(__name__)
application.register_blueprint(blacklists_blueprint)


@application.errorhandler(ApiError)
def handle_exception(err):
    response = {"msg": err.description}
    return jsonify(response), err.code


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    application.run(port=5000, debug=True)
