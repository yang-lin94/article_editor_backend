from flask_restful import Resource

from api.resources.parsers import parser
# from api.common


message = []

class Message(Resource):

    def get(self, id=None):
        if id is None:
            return {'messages': message}
        for msg in message:
            if msg['id'] == id:
                return msg
        return {'error': 'Message not found'}, 404


    def post(self):
        data = parser.parse_args()
        new_msg = {
            'id': len(message) + 1,
            'content': data['content'],
            'author': data['author']
        }
        message.append(new_msg)
        return new_msg, 201


    def delete(self, id):
        message = [msg for msg in message if msg['id'] != id]
        return {'message': 'message deleted'}
