import os
import pytest
from file_manager import FileManager


@pytest.fixture(scope="module")
def file_fixture():
    file_path = "test_file.txt"
    with FileManager(file_path, "w") as file:
        file.write("This is a test file.")
    yield file_path
    os.remove(file_path)


def test_file_contents(file_fixture):
    with FileManager(file_fixture, "r") as file:
        contents = file.read()
    assert contents == "This is a test file."
