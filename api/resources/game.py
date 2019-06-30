from flask_restplus import Namespace
from flask_restplus import Resource
from http import HTTPStatus

play_ns = Namespace("play", description="Game logic for tictactoe")


@play_ns.route("")
class Play(Resource):
    @play_ns.doc()
    def get(self):
        return HTTPStatus.OK
