from app.api.models import Game


def test_expected_behavour(player1, player2, session):
    g = Game()
    g.save_to_db()

    assert g.state == g.State.WAITING