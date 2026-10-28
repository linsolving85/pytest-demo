import pytest
from fastapi.testclient import TestClient

from app.main import app, EVENTS
from tests.test_events import make_event

client = TestClient(app)


@pytest.mark.parametrize("site, expected", [
    ("松年長照中心", 201),      # 正常
    ("松年長照中心二館", 201),    # 正常
    ("", 422),          # 空字串
    ("   ", 422),       # 只有空格
], ids=["normal_1", "normal_2", "empty", "spaces"])
def test_site(site, expected):
    EVENTS.clear()
    r = client.post("/events", json=make_event(site=site))
    assert r.status_code == expected