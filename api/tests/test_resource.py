from http import HTTPStatus


def test_get_game(client):
    response = client.get("/play")
    assert response.status_code == HTTPStatus.OK
