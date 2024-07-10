from sqlalchemy import select

from fast_api.models import User


def test_create_user(session):
    user = User(
        username='matheus',
        email='matheus@lopes.com',
        password='asdfjklç',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'matheus@lopes.com')
    )

    assert result.username == 'matheus'
