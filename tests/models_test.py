import pytest

from app.api.models import Game, Player


@pytest.fixture
def player1(grid_factory):
    return Player(name='p1', grid=grid_factory())


@pytest.fixture
def player2(grid_factory):
    return Player(name='p2', grid=grid_factory())


def test_expected_behaviour(player1, player2, session):
    g = Game()
    g.save_to_db()
    assert g.state == g.state.WAITING
