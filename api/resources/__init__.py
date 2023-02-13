from flask import Blueprint
from flask_restful import Api

from api.resources.message import Message

main = Blueprint('main', __name__)

api = Api(main)

api.add_resource(Message, '/message/', '/message/<int:id>/')