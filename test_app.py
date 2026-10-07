from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Employee Management" in response.data
    assert b"EmployeeHub" in response.data


def test_get_employees():
    client = app.test_client()

    response = client.get("/employees")

    assert response.status_code == 200
    assert len(response.json) == 4


def test_get_employee():
    client = app.test_client()

    response = client.get("/employees/1")

    assert response.status_code == 200
    assert response.json["name"] == "Anas Qureshi"


def test_employee_not_found():
    client = app.test_client()

    response = client.get("/employees/100")

    assert response.status_code == 404