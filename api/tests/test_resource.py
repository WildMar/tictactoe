from http import HTTPStatus


def test_get_game(client):
    response = client.get("/game")
    assert response.status_code == HTTPStatus.OK


def test_post_game(client):
    params = dict(row1=["___", "___", "___"],
                  row2=["___", "___", "___"],
                  row3=["___", "___", "___"],
                  move_number=1)
    response = client.post("/game", json=params)

    assert response.json.get("board") == [["___", "___", "___"], ["___", "X", "___"], ["___", "___", "___"]]
    assert response.status_code == 200


def test_post_game__missing_params(client):
    params = dict(row1=["___", "___", "___"],
                  row3=["___", "___", "___"],
                  move_number=1)

    response = client.post("/game", json=params)
    assert response.status_code == 400
