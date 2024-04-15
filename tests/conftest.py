from datetime import datetime

from django.utils import timezone

import pytest


def mock_shared_task(*args):
    def delay():
        pass


@pytest.fixture(autouse=True)
def mock_timezone_now(monkeypatch):
    class MockedDatetime(datetime):
        @classmethod
        def now(cls, tz=None):
            return timezone.make_aware(datetime(2023, 7, 7, 9, 0, 0, tzinfo=tz))

    monkeypatch.setattr("django.utils.timezone.now", MockedDatetime.now)


@pytest.fixture(autouse=True)
def mock_shared_task(monkeypatch):
    monkeypatch.setattr("celery.shared_task", mock_shared_task)
