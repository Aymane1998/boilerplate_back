from datetime import datetime

from django.utils import timezone

import pytest


def mock_delay_function(*args):
    return None


@pytest.fixture(autouse=True)
def mock_timezone_now(monkeypatch):
    class MockedDatetime(datetime):
        @classmethod
        def now(cls, tz=None):
            return timezone.make_aware(datetime(2023, 7, 7, 9, 0, 0, tzinfo=tz))

    monkeypatch.setattr("django.utils.timezone.now", MockedDatetime.now)

    monkeypatch.setattr(
        "notification.tasks.send_multiple_mails.delay", mock_delay_function
    )
