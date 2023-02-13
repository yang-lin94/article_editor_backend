from flask_restful import Resource, reqparse


class Story(Resource):
    def get(self, id):
        return {'hello': id}

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        args = parser.parse_args()
        title = {'title': args['title']}
        return title

    def delete(self, id):
        return {'result': True}