import pytest

from fastapi.testclient import TestClient

from app.entry import prepare_app


@pytest.fixture(scope='session')
def tst_client():
    test_app = prepare_app()
    with TestClient(test_app) as client:
        yield client
