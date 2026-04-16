import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    baseline = copy.deepcopy(activities)

    yield

    activities.clear()
    activities.update(baseline)


@pytest.fixture
def valid_activity_name():
    return "Chess Club"


@pytest.fixture
def unknown_activity_name():
    return "Unknown Club"


@pytest.fixture
def registered_email():
    return "michael@mergington.edu"


@pytest.fixture
def unregistered_email():
    return "new.student@mergington.edu"
