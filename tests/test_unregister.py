from src.app import activities


def test_unregister_removes_existing_participant(client, valid_activity_name, registered_email):
    # Arrange
    endpoint = f"/activities/{valid_activity_name}/signup"
    params = {"email": registered_email}

    # Act
    response = client.delete(endpoint, params=params)

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Unregistered {registered_email} from {valid_activity_name}"
    }
    assert registered_email not in activities[valid_activity_name]["participants"]


def test_unregister_returns_404_for_unknown_activity(client, unknown_activity_name, registered_email):
    # Arrange
    endpoint = f"/activities/{unknown_activity_name}/signup"
    params = {"email": registered_email}

    # Act
    response = client.delete(endpoint, params=params)

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_returns_404_for_non_registered_participant(client, valid_activity_name, unregistered_email):
    # Arrange
    endpoint = f"/activities/{valid_activity_name}/signup"
    params = {"email": unregistered_email}

    # Act
    response = client.delete(endpoint, params=params)

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Student is not signed up for this activity"}


def test_unregister_returns_422_when_email_missing(client, valid_activity_name):
    # Arrange
    endpoint = f"/activities/{valid_activity_name}/signup"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 422
