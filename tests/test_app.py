from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Flea',
            'email': 'flea@rhcp.com',
            'password': 'GiveItAway',
        },
    )  # Act

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'Flea',
        'email': 'flea@rhcp.com',
    }


def test_read_users(client):
    response = client.get('/users/')  # Act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'username': 'Flea',
             'email': 'flea@rhcp.com',
             'id': 1}
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')  # Act

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'Flea',
        'email': 'flea@rhcp.com'
    }


def test_read_user_http_404(client):
    response = client.get('/users/2')  # Act

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Júnior Groovador',
            'email': 'Groovador@rhcp.com',
            'password': '123',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'Júnior Groovador',
        'email': 'Groovador@rhcp.com',
        'id': 1,
    }


def test_update_user_http_404(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'Flea',
            'email': 'flea@rhcp.com',
            'password': 'GiveItAway',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1/')

    assert response.json() == {'message': 'User deleted'}


def test_delete_user_http_404(client):
    response = client.delete('/users/1/')

    assert response.json() == {'detail': 'User not found'}
