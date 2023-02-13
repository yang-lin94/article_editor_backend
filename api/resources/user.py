from flask_restful import Resource, reqparse

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, password={self.password})"