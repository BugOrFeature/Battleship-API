from flask import current_app, jsonify
from app.api import bp
from app.api.models import Game


@bp.route('/games/', methods=['GET'])
def status(data):
    pass


@bp.route('/games/', methods=['POST'])
def create(data):
    pass


@bp.route('/games/', methods=['PATCH'])
def move():
    pass

