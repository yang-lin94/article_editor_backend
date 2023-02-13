from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('content', type=str, required=True, help="This field cannot be left blank!")
parser.add_argument('author', type=str, required=True, help="This field cannot be left blank!")