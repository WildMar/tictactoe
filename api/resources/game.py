from http import HTTPStatus

from flask import request
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields

from .controller import Play

game_ns = Namespace("game", description="Game logic for tictactoe")

play_fields = game_ns.model("Game", {
    "row1": fields.List(fields.String, description="First row of board", required=True),
    "row2": fields.List(fields.String, description="First row of board", required=True),
    "row3": fields.List(fields.String, description="First row of board", required=True),
    "move_number": fields.Integer(description="Move number", required=True),
})


@game_ns.route("")
class Game(Resource):
    @game_ns.doc()
    def get(self):
        return HTTPStatus.OK

    @game_ns.expect(play_fields, validate=True)
    def post(self):
        move_number = request.json.get("move_number")
        board = [request.json.get("row1"), request.json.get("row2"), request.json.get("row3")]
        print(board)
        new_board, game_status = Play(player="X", move_number=move_number, board=board).calculate_next_move()
        print(new_board)
        return dict(board=new_board, game_status=game_status, status_code=200)
