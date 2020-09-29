import pytest
import os

STUBS_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "stubs")


@pytest.fixture(scope="session")
def open_file():
    def wrapper(file_name: str):
        path = os.path.join(STUBS_PATH, file_name)
        with open(path) as file:
            return file.read()

    return wrapper


@pytest.fixture
def pravda_rss(open_file):
    return open_file("stub_pravda_rss.xml")


@pytest.fixture
def unian_rss(open_file):
    return open_file("stub_unian_rss.xml")
