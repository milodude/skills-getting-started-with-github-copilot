def test_get_activities_returns_expected_structure(client, valid_activity_name):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert valid_activity_name in payload

    sample_activity = payload[valid_activity_name]
    assert "description" in sample_activity
    assert "schedule" in sample_activity
    assert "max_participants" in sample_activity
    assert "participants" in sample_activity
    assert isinstance(sample_activity["participants"], list)
