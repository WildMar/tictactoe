import pytest

from app.app import create_app


@pytest.fixture
def app():
    """ Testing fixture for pytest """
    app = create_app()
    return app


@pytest.fixture(autouse=True)
def mock_random_choice(mocker):
    """ Mock random.choice in the controller module to better predict the position of the calculated counter"""
    mocker.patch("api.resources.controller.random.choice", return_value=0)
