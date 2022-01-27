from app import app

def test1():
    """
    tests to see if our web application homepage is working
    :return:
    """
    response = app.test_client().get('/')
    assert response.status_code == 200

def test2():
    """
    tests to see if our web application edit page is working
    :return:
    """
    response = app.test_client().get('/edit')
    assert response.status_code == 200

def test3():
    """
    checks if our webpage has some key elements
    :return:
    """
    response = app.test_client().get("/edit")
    assert b"To Do App" in response.data
    assert b"Task Title" in response.data
    assert b"Add" in response.data