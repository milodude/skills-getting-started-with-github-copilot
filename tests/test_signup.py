from src.app import activities


def test_signup_adds_new_participant(client, valid_activity_name, unregistered_email):
    # Arrange
    endpoint = f"/activities/{valid_activity_name}/signup"
    params = {"email": unregistered_email}

    # Act
    response = client.post(endpoint, params=params)

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Signed up {unregistered_email} for {valid_activity_name}"
    }
    assert unregistered_email in activities[valid_activity_name]["participants"]


def test_signup_returns_404_for_unknown_activity(client, unknown_activity_name, unregistered_email):
    # Arrange
    endpoint = f"/activities/{unknown_activity_name}/signup"
    params = {"email": unregistered_email}

    # Act
    response = client.post(endpoint, params=params)

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_signup_returns_400_for_duplicate_participant(client, valid_activity_name, registered_email):
    # Arrange
    endpoint = f"/activities/{valid_activity_name}/signup"
    params = {"email": registered_email}

    # Act
    response = client.post(endpoint, params=params)

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up for this activity"}


def test_signup_returns_422_when_email_missing(client, valid_activity_name):
    # Arrange
    endpoint = f"/activities/{valid_activity_name}/signup"

    # Act
    response = client.post(endpoint)

    # Assert
    assert response.status_code == 422
