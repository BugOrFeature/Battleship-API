import requests
import json

session = requests.session()


def test_game():
        grid = "CCCCC.....BBBB......RRR.......SSS.......DD.........................................................."
        data = {'name': 'player1',
                'grid': str(grid)}
        create_game = session.post("http://127.0.0.1:5000/api/games/", json=data)
        create_game_content = json.loads(create_game.content)
        assert create_game_content['message'] == 'game created!'


def test_join():
        grid = "CCCCC.....BBBB......RRR.......SSS.......DD.........................................................."
        data = {'name': 'player2',
                'grid': str(grid)}
        join = session.post("http://127.0.0.1:5000/api/games/", json=data)
        join_content = json.loads(join.content)
        assert join_content['message'] == 'game created!'


def test_game_status():
        data = {'name': 'player1', 'game_id': 1}
        game_status = session.get("http://127.0.0.1:5000/api/games/", json=data)
        api_response = json.loads(game_status.content)
        assert api_response['state'] == 'State.PLAYING'


def test_attack():
        data = {'name': 'player1', 'game_id': 1, 'x': 0, 'y': 0}
        game_attack = session.patch("http://127.0.0.1:5000/api/games/", json=data)
        api_game_attack_response = json.loads(game_attack.content)
        assert api_game_attack_response['result'] == 'Hit Carrier'

