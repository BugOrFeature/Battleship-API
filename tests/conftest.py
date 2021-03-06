import pytest

from app.api.models import Board, Player


@pytest.fixture(scope='module')
def app():
    from app import create_app

    app = create_app()

    ctx = app.app_context()
    ctx.push()

    yield app
    ctx.pop()


@pytest.fixture(scope='module')
def db(app):
    from app import db as _db
    _db.create_all()
    yield _db
    _db.drop_all()


@pytest.fixture()
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    session = db.create_scoped_session(options={'bind': connection, 'binds': {}})
    db.session = session

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope='module')
def test_client(app):
    return app.test_client()


@pytest.fixture
def player1(grid_factory):
    return Player(name='player1', grid=grid_factory())


@pytest.fixture
def player2(grid_factory):
    return Player(name='player2', grid=grid_factory())


@pytest.fixture
def board_factory():
    standard_grid =  'CCCCCSSSDD' \
                   + 'BBBBRRR...' \
                   + '..........' \
                   + '..........' \
                   + '..........' \
                   + '..........' \
                   + '..........' \
                   + '..........' \
                   + '..........' \
                   + '..........'

    def create(grid: str = standard_grid):
        return Board(grid)

    return create