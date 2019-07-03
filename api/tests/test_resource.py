from http import HTTPStatus


def test_get_game(client):
    response = client.get("/game")
    assert response.status_code == HTTPStatus.OK


def test_post_game(client):
    params = dict(row1=["", "", ""],
                  row2=["", "", ""],
                  row3=["", "", ""],
                  move_number=1)
    response = client.post("/game", json=params)

    assert response.json.get("board") == [["", "", ""], ["", "X", ""], ["", "", ""]]
    assert response.status_code == 200


def test_post_game__missing_params(client):
    params = dict(row1=["", "", ""],
                  row3=["", "", ""],
                  move_number=1)

    response = client.post("/game", json=params)
    assert response.status_code == 400
